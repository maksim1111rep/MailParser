import logging
def logging_settings():
    logging.basicConfig(level=logging.INFO,
                        filename="mailparser.log",
                        filemode="a",
                        format="%(asctime)s-%(levelname)s-%(name)s-%(message)s",
                        encoding="utf-8"
                        )
logger=logging.getLogger("MailParser")


