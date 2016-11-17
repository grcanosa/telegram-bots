#!/usr/bin/python3

import logging;
import random
from .cmdprocessor import CmdProcessor;


class PhraseList(CmdProcessor):
    def __init__(self,cmd,list,phrasetype="message"):
        super().__init__(cmd);
        self._cmd = cmd;
        self._list = list;
        self._type = phrasetype;

    def get_random_phrase(self):
        return random.choice(self._list);

    def process(self,userR,bot,update):
        ret = False;
        if self.cmd_ok(update.message.text):
            userR.inc_cmd(update.message.from_user.id,self._cmd);
            phrasetype = self._type;
            text = "";
            logging.debug("Cmd %s RECEIVED",self._cmd);
            if userR.is_cmd_max_num(update.message.from_user.id,self._cmd):
                text+=self.get_random_phrase();
            else:
                text, phrasetype = self.get_max_cmd_response(update);
            ret = True;
            if phrasetype == "message":
                bot.send_message(chat_id=update.message.chat_id,text=text);
            elif phrasetype == "gif":
                bot.send_document(chat_id=update.message.chat_id,document=text);
            elif phrasetype == "voice":
                bot.sendVoice(chat_id=update.message.chat_id,voice=text)
            elif phrasetype == "audio":
                bot.send_audio(chat_id=update.message.chat_id,audio=text);
            else:
                ret = False;
        return ret;
