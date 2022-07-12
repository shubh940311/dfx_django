from django.shortcuts import render
from .forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
import matplotlib.pyplot as plt
import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
# import wx
import matplotlib.font_manager
import glob
import re
from ezdxf.addons.drawing.properties import Properties, LayoutProperties
import os


# Create your views here.

def hotel_image_view(request):
  
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    
    image = os.path.dirname(__file__)

    new_path = image + "\images"
    print('image',new_path)
    list_of_files = glob.glob(f"{new_path}\*") # * means all if need specific format then *.csv
    print(list_of_files)
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    convert_dxf2img(latest_file)
    return render(request, 'image.html', {'form' : form})


default_img_format = '.png'
default_img_res = 300
default_bg_color = '#FFFFFF'
def convert_dxf2img(name, img_format=default_img_format, img_res=default_img_res,clr=default_bg_color):
            doc = ezdxf.readfile(name)
            msp = doc.modelspace()
            # Recommended: audit & repair DXF document before rendering
            auditor = doc.audit()
            # The auditor.errors attribute stores severe errors,
            # which *may* raise exceptions when rendering.
            if len(auditor.errors) != 0:
                raise Exception("This DXF document is damaged and can't be converted! --> ", name)
                name = name =+ 1
            else :

                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                ctx = RenderContext(doc)
                ctx.set_current_layout(msp)

                ezdxf.addons.drawing.properties.MODEL_SPACE_BG_COLOR = clr
                out = MatplotlibBackend(ax)
                print("in middle2")

                Frontend(ctx, out).draw_layout(msp, finalize=True)
                print("in middle3")


                # img_name = re.findall("(\S+)\.",name)  # select the image name that is the same as the dxf file name
                # img_name = "F:\\workspace\\dxf\\trial4\\result"
                  # select the image name that is the same as the dxf file name
                image = os.path.dirname(__file__)

                img_name = image + "\data\myconversion"

                first_param = ''.join(img_name) + img_format  #concatenate list and string
                fig.savefig(first_param, dpi=img_res)
                print(name," Converted Successfully")


    


    
  
  
def success(request):
    return HttpResponse('successfully uploaded')
