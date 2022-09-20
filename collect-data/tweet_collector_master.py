import tweepy
import os
from dotenv import load_dotenv
# import csv

# Twitter API credentials
load_dotenv()
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_key = os.getenv("ACCESS_KEY")
access_secret = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# screen_name = "@PrimeministerGR"


anel = ["@anexartitoi", "@angelou2004_m", "@ElenaKountoura", "@GeorgeVagiakis", "@ilarxos3", "@MariaKolliaTsar",
        "@PanosKammenos", "@TerensQuick", "@VASILISKOKKALHS", "@XRHSTOS_ST"]
nd = ["@AdonisGeorgiadi", "@AnnaAsimakopoul", "@Avramopoulos", "@cstaikouras", "@Dora_Bakoyannis", "@gioulekaskostas",
      "@gkefalogiannis", "@GKoumoutsakos", "@K_Hatzidakis", "@KalafatisSt", "@kmitsotakis", "@MakisVoridis",
      "@MariaSpyraki", "@MVarvitsiotis", "@neademokratia", "@NikosDendias", "@nkaklamanis", "@olgakef",
      "@samaras_antonis", "@SimosKedikoglou", "@thanosplevris", "@TheoKaraoglou", "@tzitzikostas", "@v_meimarakis",
      "@Vkikilias",
      "@vozemberg", "@fortsakis", "@stamatis_dim", "@nkerameus", "@OikonomouVasili", "@OikonomouB", "@AnnaKaramanli",
      "@GerGiakoumatos", "@SalmasMarios", "@k_karagounis", "@gstylios", "@GeorgiaMartinou", "@Vlachos_G", "@athbouras",
      "@IasonFotilas", "@kutsubad", "@kyriazidisdim", "@manoskonsolas", "@a_vesiropoulos", "@l_avgenakis",
      "@giogiakasv", "@savanastasiadis", "@kat_markou", "@npanagioto", "@tsiaras_kostas", "@MarAntoniou",
      "@ChristosDimas_",
      "@VroutsisGiannis", "@adavakis", "@pantamaximos", "@kellas_xristos", "@G_Plakiotakis", "@XarAthan",
      "@chboukoros1", "@katsafados", "@nmitarakis", "@ArampatziFotini", "@KostasSkrekas", "@GVagionas"]
pasok = ["@a_loverdos", "@androulakisnick", "@BKegeroglou", "@EvaKaili", "@EVenizelos", "@evichrist", "@FofiGennimata",
         "@koukoulopoulos", "@KSkandalidis", "@Odysseas_", "@papatheodorou_t", "@pasok", "@dkonstantop",
         "@Yannis_Maniatis",
         "@KremastinosD", "@koutsoukosilia", "@lgrigorakos", "@ILHANAHMET", "@MTZELEPIS", "@Arvanitidis_Geo"]
syriza = ["@annetakavadia", "@atsipras", "@c_spirtzis", "@ChVernardakis", "@CZachariadis", "@d_tzanakopoulos",
          "@g_stathakis", "@g_vassiliadis", "@gkatr", "@kkuneva", "@MarkosBolaris", "@nikos_toskas", "@NikosKotzias",
          "@nikoxy",
          "@olgagerovasili", "@panos_rigas", "@PanosSkourolia1", "@papadimoulis", "@pkonstantineas7",
          "@PrimeministerGR", "@pskourl", "@rania_sv", "@renadourou", "@SFamellos", "@SteliosKoul", "@syriza_gr",
          "@tsakalotos", "@TsironisGianni",
          "@YDragasakis", "@katenotopoulou", "@nectarsant", "@cbgialas", "@gpantzas", "@giorgoskyritsis", "@ybalafas",
          "@kouroumplis", "@EleniAvlonitou", "@nasosa8anasiou", "@sia_anag", "@TheanoFotiou", "@MBalaouras",
          "@sokrvardakis",
          "@marios_katsis", "@Amanatidis_Gian", "@tasoskourakis", "@tr_alexandros", "@mardas55", "@dgakis",
          "@kaisasgeorgios", "@vag_apos", "@geakriotis", "@zlivaniou", "@A_Meikopoulos", "@SGiannakidis",
          "@sgiannakidis85", "@stogiannidisgr2",
          "@elen_stamataki", "@syrmal2000", "@FotiniVaki", "@mtheleriti", "@g_psychogios", "@p_dritseli",
          "@akaranastasis", "@dimvett", "@pavpol2222", "@g_stathakis", "@igglezi", "@k0stopanagiotou", "@JSarakiotis",
          "@Michelis_Athan",
          "@XrSimorelis", "@sakis_papad", "@kaisasgeorgios", "@PanosSkourolia1", "@FKarasarlidou", "@MBalaouras",
          "@andreasxanthos", "@kostasbarkas", "@Ggennia", "@dimitrisvitsas", "@EviKarakosta"]
syriza2 = ["@sgiannakidis85", "@stogiannidisgr2", "@elen_stamataki", "@syrmal2000", "@FotiniVaki", "@mtheleriti",
           "@g_psychogios", "@p_dritseli", "@akaranastasis", "@dimvett", "@pavpol2222",
           "@g_stathakis", "@igglezi", "@k0stopanagiotou", "@JSarakiotis", "@Michelis_Athan", "@XrSimorelis",
           "@sakis_papad", "@kaisasgeorgios", "@PanosSkourolia1", "@FKarasarlidou", "@MBalaouras", "@andreasxanthos",
           "@kostasbarkas", "@Ggennia", "@dimitrisvitsas", "@EviKarakosta"]
# xa = ["@AntonisGregos", "@Barbarousis", "@EleniZaroulia", "@EpitidGeorgios", "@FountoulisLampr", "@GermenisGiorgos", "@IliasKasidiaris", "@ipanagiotaros", "@johnsaxinidis", "@PappasXA", "@xrhstospappas", "@Panagiotisiliop",
#      "@ipanagiotaros", "@IAIVATIDIS", "@XA_KILKIS"]
xa = ["@FountoulisLampr", "@GermenisGiorgos", "@IliasKasidiaris", "@ipanagiotaros", "@johnsaxinidis", "@PappasXA",
      "@xrhstospappas", "@Panagiotisiliop",
      "@ipanagiotaros", "@IAIVATIDIS", "@XA_KILKIS"]

for member in pasok:
    screen_name = member
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    # transform the tweepy tweets into a 2D array that will populate the csv
    # outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    # outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]
    outtweets = [[tweet.created_at, tweet.text] for tweet in alltweets]

    f = open('%s_tweets.txt' % screen_name, 'a', encoding='utf-8')
    for tweet in outtweets:
        f.write(str(tweet))
        f.write('\n')
    f.close()

# write the csv
# with open('%s_tweets.csv' % screen_name, 'w', encoding='utf-8') as f:
#	writer = csv.writer(f)
#	writer.writerow(["id","created_at","text"])
#	writer.writerows(outtweets)
