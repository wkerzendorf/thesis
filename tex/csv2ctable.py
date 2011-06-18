
ctable_header="""\ctable[
    cap = {cap}
    caption = {caption}
    label = {label}
    pos = {pos}
    ]"""
    
def data2ctable(data, **kwargs):
    format_dict = {'cap':'short caption',
                'caption':'long caption',
                'label':'label',
                'pos':'ht',
                'align':'c',
                'descr':None}
    format_dict.update(kwargs)
    fields = list(test.dtype.fields)
    ctable = "" + ctable_header.format(**format_dict)
    align = format_dict['align']
    if len(align) == 1:
        ctable +='{%s}{}{\FL\n' % (align*(len(fields)+1))
    else:
        ctable +='{%s}{}{\FL\n' % (align)
    
    ctable += '&'+' & '.join(map(str, fields)) + '\n'
    
    if format_dict['descr']!=None:
        ctable += '&'+' & '.join(map(str, format_dict['descr'])) + '\n'
        
    ctable += '\ML\n'
    
    for line in data:
        ctable += '&'+' & '.join(map(str, line)) + '\NN\n'
        
    return ctable+'\LL}\n'
    
    