from rest_framework import authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .bsbot.model import response
from .models import FAQs


@api_view(['POST'])
@authentication_classes([authentication.SessionAuthentication, authentication.BasicAuthentication])
@permission_classes((IsAuthenticated,))
def chatbot(request):
    # get the question form the input field
    question = request.data.get('question', '')
    # strip the string
    question = question.strip()
    # get an answer form the chatbot model
    answer = response(question)
    # if the chatbot don´t know the answer
    if not answer:
        answer = 'Das weiß ich leider nicht! Aber unsere Mitarbeiter Beraten dich gerne! Ruf uns gleich an: 0676/ 123 45 67'
    # Save every new question to FAQS
    if question:
        FAQs.objects.get_or_create(question=question)
    return Response({"answer": answer})
