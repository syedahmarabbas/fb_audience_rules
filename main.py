from fb_audience_rule import Filter, Filters


def regex_generator(min_price: int) -> str:
    search = str(min_price)
    search_len = len(search)
    out_regex = 'precio-desde_(' + '\d{' + str((search_len + 1)) + ',}|'
    idx = -1
    for i in range(search_len - 1, 0, -1):
        my_str = ''
        for j in range(i):
            my_str = my_str + search[j]
        if i == search_len - 1:
            str_value = search[i]
        else:
            str_value = str(int(search[i]) + 1)

        out_regex = out_regex + my_str + '[' + str_value + '-9]' + '\d{' + str((idx + 1)) + ',}|'
        idx = idx + 1
    out_regex = out_regex + '[' + search[i] + '-9]' + '\d{' + str((idx + 1)) + ',}'
    out_regex = out_regex + ')'
    return out_regex


def get_filter(min_price: int = None, max_price: int = None, currency: str = None):
    if min_price is None and max_price is None:
        value_error = ValueError()
        value_error.strerror = "Both min and max searches can't be null"
        raise value_error
    _currency = 'moneda_' + currency.lower()
    filters_list = [Filters(field="url",
                            operator="regex_match",
                            value=regex_generator(min_price)).dict(),
                    Filters(field="url",
                            operator="i_contains",
                            value="operacion_venta").dict(),
                    Filters(field="url",
                            operator="i_contains",
                            value=_currency).dict()]
    fb_filter = Filter(operator="and",
                    filters=filters_list).dict()
    return fb_filter


if __name__ == '__main__':
    print(get_filter(5678, currency="MXN"))
