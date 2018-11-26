# -*- coding: utf-8 -*-

class bcolors:
    HEADER = '\033[93m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


print(bcolors.HEADER + "Warning: No active frommets remain. Continue?"
+ bcolors.ENDC)