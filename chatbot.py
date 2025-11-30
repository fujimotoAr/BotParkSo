# Reference : https://github.com/Apoorva-Udupa/rule_based_chatbot/blob/main/Rule_based_Bot.ipynb

import re

class RuleBot:
  ### Potential Negative Responses
  negative_responses = ("tidak", "bukan", "ganti")
  exit_commands = ("exit", "selesai", "keluar","terima kasih","cukup", "sekian", "clear")

  # Define the random questions and corresponding responses
  normalize_dict = {
      ("Halo", "Hai", "Pagi", "Siang", "Hi", "konnichiwa", "kamu siapa", "ini apa", "bot apa", "anata dare"): "Halo juga... Kenalin aku BotParkSo (Bot Parking Solution) 🤗🤗🤗 \n\nAku akan membantu memberikan rekomendasi parkir bagi Civitas Akademika di Wilayah Kampus UGM... \n\nSilakan pilih jenis kendaraannya dulu ya 🛵🏍️🚗 ↴↴↴ \n\nketik 1 → sepeda motor \n\nketik 2 → mobil \n\nketik 3 → sepeda \n\nBot tunggu dengan senang hati tanggapannya 🤗🤗🤗",

      #1:sepeda motor 2:mobil 3:sepeda
      ("1","2","3"):"Untuk melanjutkan BotParkSo sedang berbincang dengan siapa? Silakan pilih ↴↴↴ \n\nketik dosen → apabila berstatus dosen \n\nketik tendik → apabila berstatus tendik \n\nketik mahasiswa → apabila berstatus mahasiswa \n\nMohon ditanggapi, hal ini sangat penting untuk memberikan rekomendasi parkir yang sesuai 🤗🤗🤗",
      ("dosen", "pengajar","mahasiswa","tendik","staff"):"Pilih lokasi untuk mengetahui rekomendasi lokasi parkir bagi Civitas Akademika UGM ↴↴↴ \n\nketik teknik → untuk lokasi sekitar Fakultas Teknik \n\nketik gsp → untuk lokasi sekitar GSP \n\nketik feb → untuk lokasi sekitar Fakultas Ekonomika dan Bisnis \n\nketik mipa → untuk lokasi sekitar Fakultas MIPA \n\nketik fkkmk → untuk lokasi sekitar Fakultas Kedokteran",
      ("teknik", "fakultas teknik", 'ft', "gijutsugakubu"): "Rekomendasi Lokasi Parkir Fakultas Teknik UGM  🚗🚙🚘 \n\n Untuk kendaraan roda empat berada di: \n\n1. utara Gedung DTGD \n\n2. utara Gedung DTGD \n\n3. utara dan selatan jalan lingkar DTAP \n\n4. selatan sekretariat BEM FT \n\n5. utara jalan lingkar DTK \n\n6. selatan dan barat Gedung B DTMI \n\n7. utara lapangan voli DTMI \n\n8. jalan lingkar DTETI \n\n9. selatan jalan lingkar DTNTF \n\n10. selatan jalan lingkar DTGL",
      ("gsp", "kptu", "gedung pusat", "feb", "keizaigakubu"): "Rekomendasi Lokasi Parkir GSP UGM 🚗🚙🚘 \n\n Untuk kendaraan roda empat berada di: \n\n1. lapangan GSP UGM \n\n2. timur dan barat Gedung GSP UGM \n\n3. sepanjang jalan utara Gedung GSP UGM",
      ("mipa", "fmipa", "fakultas mipa", "rigakubu"): "parkiran fakultas mipa UGM",
      ("fkkmk", "kedokteran", "fakultas kedokteran", "igakubu"): "parkiran kantong parkir Jl. Kesehatan"
  }
  def __init__(self):
    #self.greeting = False
    self.has_greeted=False

  def greeting(self):
    #self.greeting = True
    self.has_greeted=True
    print("Halo... Ada yang bisa dibantu?")

  def normalize(self, input):
    input = input.lower()
    input = re.sub(r"([?.!,])", r" \1 ", input)
    input = re.sub(r"\s{2,}", " ", input)
    return input

  def is_negative(self, reply):
    for command in self.negative_responses:
      if reply == command:
        return True

  def is_exit(self, reply):
    for command in self.exit_commands:
      if reply == command:
        return True

  def get_response(self, input):
    for keys in self.normalize_dict.keys():
      for key in keys:
        if self.normalize(self, input) in self.normalize(self, key):
          return self.normalize_dict[keys]

  def start_chat(self):
      self.greeting()
      exit = False
      while not exit:
          user_input = input("Tanggapan: ")

          if self.is_negative(user_input):
            continue

          if self.is_exit(user_input):
            exit=True
            continue

          print(self.get_response(user_input))