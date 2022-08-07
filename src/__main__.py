from src.webservice.webservice import OcrService
uci_service = OcrService(name="ocr")
uci_service.prepare_pipeline_config("./config.yml")
uci_service.run_service()