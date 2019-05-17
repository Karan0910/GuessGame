class Table(object):
    def format_as_table(self,data,
                        header,keys):
   
        # If header is not empty, add header to data
        if header:
            # Get the length of each header and create a divider based
            # on that length
            header_divider = []
            for name in header:
                header_divider.append('-' * len(name))

            # Create a list of dictionary from the keys and the header and
            # insert it at the beginning of the list. Do the same for the
            # divider and insert below the header.
            header_divider = dict(zip(keys, header_divider))
            data.insert(0, header_divider)
            header = dict(zip(keys, header))
            data.insert(0, header)

        column_widths = []
        for key in keys:
            column_widths.append(max(len(str(column[key])) for column in data))

        # Create a tuple pair of key and the associated column width for it
        key_width_pair = zip(keys, column_widths)

        format = ('%%-*s ' * len(keys)).strip() + '\n'
        formatted_data = ''
        for element in data:
            data_to_format = []
            # Create a tuple that will be used for the formatting in
            # width, value format
            for pair in key_width_pair:
                data_to_format.append(pair[1])
                data_to_format.append(element[pair[0]])
            formatted_data =formatted_data.format(tuple(data_to_format))
        return formatted_data