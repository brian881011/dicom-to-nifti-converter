import dicom2nifti
import os
from pydicom import dcmread

current_dir = os.getcwd()

for patient in os.listdir(current_dir):

	#print(patient) #ex:0009

	if not os.path.isdir(patient):
		continue
	patient_dir = os.path.join(current_dir, patient)
	for case in os.listdir(patient_dir):

		#print(case) #ex:SE3_LungCARE_1mm_Axial_1.0 

		case_dir = os.path.join(patient_dir, case)
		if not os.path.isdir(case_dir):
			continue
		for dcm in os.listdir(case_dir):
			dcm_path = os.path.join(case_dir, dcm)
			ds = dcmread(dcm_path)

			date = ds[0x0040,0x0002].value
			thickness = str(int(ds[0x0018,0x0050].value))
			pid = ds[0x0010,0x0020].value
			break
		new_dir = pid+"-"+date+"-"+thickness+"mm.nii.gz"
		dicom2nifti.dicom_series_to_nifti(case_dir, new_dir)

		#if not os.path.isdir(new_dir):
			#os.mkdir(pid+"-"+date+"-"+thickness+"mm-nii")

