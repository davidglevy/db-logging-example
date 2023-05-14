import logging

def setup_logging(level=logging.INFO):
    """
        Setup the logger for use within notebooks, also turns up level for py4j.clientserver

        @param: level you can override the default of logging.INFO
    """

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logging.getLogger("py4j.clientserver").setLevel(logging.WARN)

    # # Logs to sys.stderr by default.
    logformat = '[%(levelname)-8s] %(asctime)s %(name)s: %(message)s' 
    handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt=logformat)
    handler.setFormatter(formatter)
    logger.handlers = [handler]
    
    # Return logger for conveinience but can also use singleton method to retrieve.
    return logger
