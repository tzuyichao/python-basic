import jpype
import jpype.imports
from jpype.types import *
import datetime

current_date = datetime.datetime.now()
date_str = current_date.strftime("%Y-%m-%d")
logpath = f"D:\\work\\MDM\\mdm-service\\target\\log-{date_str}.txt"
path = 'D:\\work\\MDM\\mdm-service\\target\\mdm-service-0.0.1-SNAPSHOT.jar'
jvmPath = jpype.getDefaultJVMPath()
jpype.startJVM(jvmPath,"-ea","-Djava.class.path=%s"%path)

from java.lang import System
from java.io import PrintStream, File

System.setOut(PrintStream(File(logpath)))

CrmControllerClass = jpype.JClass("com.deltaww.mdm.controller.CrmController")

crmController = CrmControllerClass()

crmController.processCrmRawData()