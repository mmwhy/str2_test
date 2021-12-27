import os
import csv

from st2common.runners.base_action import Action

__all__ = [
    'SaveTXTFileAction'
]


class SaveTXTFileAction(Action):
    def run(self, greeting):
        f = open('result.txt', mode='w', encoding='utf-8')
        f.write(greeting)  # write 写入
        f.close()

        return greeting