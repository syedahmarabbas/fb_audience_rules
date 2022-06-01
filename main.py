import re

from fb_audience_rule import Filter, Filters


def regex_generator_lt(price, term_string="precio-desde") -> str:
    search = str(price)
    search_len = len(search)
    filters = []
    for i in range(search_len - 1, -1, -1):
        filters.append("\d{" + str(i) + "}")
        s = search[:i]
        q = int(search[i])
        if q == 0:
            continue
        if q == 1:
            mx = "0"
        else:
            mx = f"[0-{q-1}]"
        flt = s + mx
        remaining_digits = search_len - len(s) - 1
        if remaining_digits > 0:
            flt += "\d{" + str(remaining_digits) + "}"
        filters.append(flt)
    filter_string = "|".join(filters)
    return f"{term_string}_({filter_string})/"


def regex_generator_gte(min_price: int, term_string="precio-desde") -> str:
    search = str(min_price)
    search_len = len(search)
    out_regex = f'{term_string}_(' + '\d{' + str((search_len + 1)) + ',}|'
    idx = -1
    for i in range(search_len - 1, -1, -1):
        my_str = ''
        for j in range(i):
            my_str = my_str + search[j]
        if i == search_len - 1:
            str_value = search[i]
        else:
            str_value = str(int(search[i]) + 1)

        out_regex = out_regex + my_str + '[' + str_value + '-9]' + '\d{' + str((idx + 1)) + ',}|'
        idx = idx + 1
    return f'[{search[0]}-9]' + '\d{' + str((idx + 1)) + ',}' + ')'


def get_filter(currency: str, min_price_f, min_price_t, max_price_f, max_price_t):
    _currency = 'moneda_' + currency.lower()
    filters_list = [
        Filters(
            field="url",
            operator="regex_match",
            value=regex_generator_gte(min_price_f)
        ),
        Filters(
            field="url",
            operator="regex_match",
            value=regex_generator_lt(min_price_t)
        ),
        Filters(
            field="url",
            operator="regex_match",
            value=regex_generator_gte(max_price_f, term_string="precio-hasta")
        ),
        Filters(
            field="url",
            operator="regex_match",
            value=regex_generator_lt(max_price_t, term_string="precio-hasta")
        ),
        Filters(
            field="url",
            operator="i_contains",
            value="operacion_venta"
        ),
        Filters(
            field="url",
            operator="i_contains",
            value=_currency
        )
    ]
    return Filter(
        operator="and",
        filters=filters_list
    ).dict()


if __name__ == '__main__':
    # print(get_filter("MXN", 200_000, 250_000, 250_000, 300_000))
    print(regex_generator_lt(200_000))
    print(regex_generator_lt(199_999))
