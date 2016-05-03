# coding: utf-8 
import os

from io import BytesIO

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table,TableStyle, Image
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import Year

from django.shortcuts import render
from django.template import loader

class YearListView(ListView):
    model = Year
    fields = '__all__'    

class YearCreateView(CreateView):
    model = Year
    fields = '__all__'

def hello_pdf(request):
    # Create the HttpResponse headers with PDF.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Platzi-student-report.pdf'

    # Create the PDF object, using the BytesIO as its "file."
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    #Header
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30, 750, 'Platzi')

    c.setFont('Helvetica', 12)
    c.drawString(30, 735, 'Report')

    c.setFont('Helvetica-Bold', 12)
    c.drawString(480, 750, "01/07/2016")
    #start X, height end y, heigth
    c.line(460, 747, 560, 747)

    #Students table
    students = [
        {'#':'1','name':'Angel Arteaga', 'b1':'3.4', 'b2':'2.4', 'b3':'5.4', 'total':'10'},
        {'#':'1','name':'Angel Arteaga', 'b1':'3.4', 'b2':'2.4', 'b3':'5.4', 'total':'10'},
        {'#':'1','name':'Angel Arteaga', 'b1':'3.4', 'b2':'2.4', 'b3':'5.4', 'total':'10'},
        {'#':'1','name':'Angel Arteaga', 'b1':'3.4', 'b2':'2.4', 'b3':'5.4', 'total':'10'},
        {'#':'1','name':'Angel Arteaga', 'b1':'3.4', 'b2':'2.4', 'b3':'5.4', 'total':'10'},
        {'#':'1','name':'Angel Arteaga', 'b1':'3.4', 'b2':'2.4', 'b3':'5.4', 'total':'10'}
    ]

    #Table header
    styles = getSampleStyleSheet()
    styleBH = styles["Normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontSize = 10

    numero = Paragraph('''#''', styleBH)
    alumno = Paragraph('''Alumno''', styleBH)
    b1 = Paragraph('''BIM1''', styleBH)
    b2 = Paragraph('''BIM2''', styleBH)
    b3 = Paragraph('''BIM3''', styleBH)
    total = Paragraph('''Promedio''', styleBH)

    data = []

    data.append([numero, alumno, b1, b2, b3, total])

    #Table
    styleN = styles["BodyText"]
    styleN.alignment = TA_CENTER
    styleN.fontSize = 7

    high = 650
    for student in students:
    	this_student = [student['#'], student['name'], student['b1'], student['b2'], student['b3'], student['total']]
    	data.append(this_student)
    	high = high - 18

    #table size
    width, heigth = A4
    table = Table(data, colWidths=[1.9 * cm, 9.5 * cm, 1.9 * cm, 1.9 * cm, 1.9 * cm, 2 * cm])
    table.setStyle(TableStyle([#estilos de la tabla
    	('INNERGRID',(0,0),(-1, -1), 0.25, colors.blue),
    	('BOX', (0,0), (-1, -1), 0.25, colors.red),]))

    #pdf size
    table.wrapOn(c, width, heigth)
    table.drawOn(c, 30, high)
    c.showPage() #save page

    #save pdf
    c.save()

    # get the value of BytesIO buffer and write response	 
    pdf = buffer.getvalue()
    c.showPage()
    buffer.close()
    response.write(pdf)
    return response# Create your views here.
