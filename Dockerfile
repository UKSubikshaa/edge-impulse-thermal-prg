FROM edgeimpulse/processing-block-python

WORKDIR /app

COPY . .

RUN pip install -r requirements.txtFROM edgeimpulse/processing-block-python

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
