from pydantic import BaseModel
import logfire as lf
from datetime import datetime

# This is the library for using logfire more easier.
# For using this library more easier, you can custom for it.
# This is Open-Sourced...As I know



class Delivery(BaseModel):
        timestamp: datetime
        dimensions: tuple[int, int]


m=Delivery(timestamp=datetime.now(),
           dimensions=['10', '20'])
timestatus= "["+str(m.timestamp.year)+"-"+str(m.timestamp.month)+"-"+str(m.timestamp.day)+" "+str(m.timestamp.hour)+":"+str(m.timestamp.minute)+":"+str(m.timestamp.second)+"] "



def initialize_Easylogger(serv_name="default"):
    lf.configure(service_name = serv_name)
    lf.instrument_pydantic()


def send_logs(Delivery=m, ctx="No message", extra_content="", ):
    lf.info(timestatus+ctx,
            extra={"timestamp": repr(Delivery.timestamp),
                   "context": extra_content}
            )   
    

def initialize_Pydantic(serv_name= ""):
    service_name=serv_name
    initialize_Easylogger(service_name)
    
    send_logs(m,"Initialized "+service_name)
    
    print(repr(m.timestamp))

    print(m.dimensions)

    Delivery(timestamp='2020-01-02T03:04:05Z',
             dimensions=['10', '10'],)
