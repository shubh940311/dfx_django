# dfx_django
1.It is an python and django created api to convert the dfx file into the png file.

2.You just need to run the command "python manage.py runserver" and then open "http://127.0.0.1:8000/image_upload/".

3.Because of this a simple UI will appear select your .dfx file and the .png file will be generated into "myproject\myapp\data".

4.The main logic part is present in views.py and inside the function named convert_dxf2img.
