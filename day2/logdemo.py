import logging

logging.basicConfig(level=logging.DEBUG,
                      filename="mylog.log",filemode='w',
        format="python-app : %(process)d  %(name)s - %(levelname)s -%(message)s - %(asctime)s" 
    )


logging.debug("Debug Error occured in code ..")
logging.info("Info: Admin logged in")
logging.warning("warning: less hard disk space .... check it")
logging.error("Error: file not found exception ")
logging.critical("Critical : app crashed")

username="Murthy"
logging.info(f" {username} has loggin in")

try:
    a=10
    b=0
    c=a/b
except Exception as ex:
    logging.error("Exception occured ",exc_info=True)
