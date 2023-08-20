from rest_framework.renderers import JSONRenderer
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context.get('response')
        status_code = response.status_code
        status_mapping = {
            200: {
                'status': 'success',
                'message': 'ok'},
            201: {
                'status': 'success',
                'message': 'accepted'},
            400: {
                'status': 'error',
                'message': 'bad request'},
            401: {
                'status': 'error',
                'message': 'unauthorized'},
            403: {
                'status': 'error',
                'message': 'forbidden'},
            404: {
                'status': 'error',
                'message': 'not found'},
            500: {
                'status': 'error',
                'message': 'internal server error'},
        }
        state = status_mapping.get(status_code)
        if state:
            status = state['status']
            message = state['message']
        else:
            status = 'info'
            message = None 
        response_data = {   
            'status': status,
            'code': status_code,
            'message': message,
            'data': data,
            'meta': {
                'version': os.getenv("API_VERSION"),
                'timestamp': datetime.timestamp(datetime.now())
            }
        }

        return super().render(response_data, accepted_media_type, renderer_context)
