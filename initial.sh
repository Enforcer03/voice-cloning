pip install -U scipy
pip install torchaudio
git clone https://github.com/jnordberg/tortoise-tts.git
cd tortoise-tts
pip install -r requirements.txt
pip install transformers==4.19.0 einops==0.5.0 rotary_embedding_torch==0.1.5 unidecode==1.3.5
python setup.py install