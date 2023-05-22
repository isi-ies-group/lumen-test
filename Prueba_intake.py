import lumen as lm
import panel as pn

pn.extension('tabulator')


sources=lm.Source(
    {
     'rockies': {
         'type':'intake',
         'shared':'true',
         'cache_dir': 'cache',
         'catalog':{
             'sources':{
                 'southern_rockies':{
                     'driver':'csv',
                     'args':{
                         'urlpath':'s3://datasets.holoviz.org/precipitation/v1/SRLCC_{emissions}_Precip_{model}.csv',
                         'csv_kwargs':{
                             'skiprows': '3', 
                             'names':['time','precip'],
                             'parse_dates':['time']
                             }                         
                         },
                     'storage_option':{
                         'anon':'true'
                         }
                     }
                 }
             }
         }
     
})
sources


pipeline = lm.Pipeline.from_spec(
{    
    'rockies': {
        'spurce': 'rockies', 
        'table':'southern_rockies',
        'filters': [
            {'type': 'widget', 'field': 'irr_sup'},
            {'type': 'widget', 'field': 'irr_fro'},
            {'type': 'widget', 'field': 'irr_tra'},
            {'type': 'widget', 'field': 'irr_der'},
            {'type': 'widget', 'field': 'irr_izq'}
        ],
    }
})
pipeline



