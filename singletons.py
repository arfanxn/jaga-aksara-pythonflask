import os
from external_modules.jaga_aksara_ai.Integration import JagaAksara 

_jaga_aksara_model:JagaAksara|None = None

def load_jaga_aksara_model() -> None :
    """
    Load Jaga Aksara model into memory.

    The model is loaded from a directory specified by the
    `JAGA_AKSARA_MODELS_DIRECTORY` environment variable.
    """
    global _jaga_aksara_model
    models_dir = os.getenv('JAGA_AKSARA_MODELS_DIRECTORY')
    _jaga_aksara_model =  JagaAksara(models_dir)

def get_jaga_aksara_model () -> JagaAksara|None :
    """
    Get the Jaga Aksara model that has been loaded into memory.

    The model is loaded from a directory specified by the
    `JAGA_AKSARA_MODELS_DIRECTORY` environment variable.

    Returns:
        JagaAksara: The Jaga Aksara model that has been loaded into memory.
        None: If the model has not been loaded yet.
    """
    global _jaga_aksara_model
    if _jaga_aksara_model is None:
        models_dir = os.getenv('JAGA_AKSARA_MODELS_DIRECTORY')
        _jaga_aksara_model =  JagaAksara(models_dir)
    return _jaga_aksara_model
