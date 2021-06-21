import os
from rest_framework._proj.cctv_prediction.services import CctvServices
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


class CctvApi(object):

    @staticmethod
    def main():
        cctv_svc = CctvServices()
        while 1:
            menu = input('[1] Seoul CCTV DF\n'
                         '[2] Seoul Crime DF\n'
                         '[3] PoliceStation DF\n'
                         '[4] Unemployment DF\n'
                         '[5] POP Seoul DF\n'
                         '[0] EXIT\n'
                         '>> ')
            if menu == '0':
                break
            elif menu == '1':
                cctv_svc.csv({'context': './data/', 'fname': 'cctv_in_seoul'})
            elif menu == '2':
                cctv_svc.csv({'context': './data/', 'fname': 'crime_in_seoul'})
            elif menu == '3':
                cctv_svc.csv({'context': './data/', 'fname': 'police_position'})
            elif menu == '4':
                cctv_svc.csv({'context': './data/', 'fname': 'us_unemployment'})
            elif menu == '5':
                cctv_svc.xls({'context': './data/', 'fname': 'pop_in_seoul'})
            else:
                continue


CctvApi.main()
