#loging
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
# loging messages

logging.debug("This is a debug message")
logging.info("This is an info message") 
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
logging.exception("This is an exception message")

#simple example
def divide(a, b):
    try:
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError as e:
        logging.error("Attempted to divide by zero.")
        logging.exception("Exception occurred")
        return None
