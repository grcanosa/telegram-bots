import emoji;
import random;
from ..handlers.phraselist import PhraseList;

NAMELIST = [
#   ":bowtie:",
   ":smile:",
#   ":simple_smile:",
   ":laughing:",
   ":blush:",
   ":smiley:",
   ":relaxed:",
   ":smirk:",
   ":heart_eyes:",
   ":kissing_heart:",
   ":kissing_closed_eyes:",
   ":flushed:",
   ":relieved:",
   ":satisfied:",
   ":grin:",
   ":wink:",
   ":stuck_out_tongue_winking_eye:",
   ":stuck_out_tongue_closed_eyes:",
   ":grinning:",
   ":kissing:",
   ":kissing_smiling_eyes:",
   ":stuck_out_tongue:",
   ":sleeping:",
   ":worried:",
   ":frowning:",
   ":anguished:",
   ":open_mouth:",
   ":grimacing:",
   ":confused:",
   ":hushed:",
   ":expressionless:",
   ":unamused:",
   ":sweat_smile:",
   ":sweat:",
   ":disappointed_relieved:",
   ":weary:",
   ":pensive:",
   ":disappointed:",
   ":confounded:",
   ":fearful:",
   ":cold_sweat:",
   ":persevere:",
   ":cry:",
   ":sob:",
   ":joy:",
   ":astonished:",
   ":scream:",
#   ":neckbeard:",
   ":tired_face:",
   ":angry:",
   ":rage:",
   ":triumph:",
   ":sleepy:",
   ":yum:",
   ":mask:",
   ":sunglasses:",
   ":dizzy_face:",
   ":imp:",
   ":smiling_imp:",
   ":neutral_face:",
   ":no_mouth:",
   ":innocent:",
":running:",
":couple:",
":family:",
":two_men_holding_hands:",
":two_women_holding_hands:",
":dancer:",
":dancers:",
":ok_woman:",
":no_good:",
":information_desk_person:",
":raising_hand:",
":bride_with_veil:",
":person_with_pouting_face:",
":person_frowning:",
":bow:",
":couplekiss:",
":couple_with_heart:",
":massage:",
":haircut:",
":nail_care:",
":boy:",
":girl:",
":woman:",
":man:",
":baby:",
":older_woman:",
":older_man:",
":person_with_blond_hair:",
":man_with_gua_pi_mao:",
":man_with_turban:",
":construction_worker:",
":cop:",
":angel:",
":princess:",
":smiley_cat:",
":smile_cat:",
":heart_eyes_cat:",
":kissing_cat:",
":smirk_cat:",
":scream_cat:",
":crying_cat_face:",
":joy_cat:",
":pouting_cat:",
":japanese_ogre:",
":japanese_goblin:",
":see_no_evil:",
":hear_no_evil:",
":speak_no_evil:",
":guardsman:",
":skull:",
":feet:",
":lips:",
":kiss:",
":droplet:",
":ear:",
":eyes:",
":nose:",
":tongue:",
":love_letter:",
":bust_in_silhouette:",
":busts_in_silhouette:",
":speech_balloon:",
":thought_balloon:"
# ":feelsgood:",
# ":finnadie:",
# ":goberserk:",
# ":godmode:",
# ":hurtrealbad:",
# ":suspect:",
# ":trollface:"
   ];




LIST = [];
for s in NAMELIST:
    LIST.append(emoji.emojize(s,use_aliases=True));

class PeopleEmoji(PhraseList):
    def __init__(self,cmd):
        super().__init__(cmd,LIST,"message");
        text = "Quieres emoji?, pues toma dos ";
        text += emoji.emojize(":coffee::coffee: \n",use_aliases=True);
        self._response = text;

    def get_max_cmd_response(self,update):
        text = self._response;
        # for i in range(1,100):
        #     text+=self.get_random_phrase();
        # text += "LALALALA";
        for e in self._list:
            text+=e
        return text,"message";
