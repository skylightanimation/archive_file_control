from app import ma

class ResponseSchema(ma.Schema):
    class Meta:
        fields = ('OUT_STAT','OUT_MESS','OUT_DATA')
        
response_schema = ResponseSchema()