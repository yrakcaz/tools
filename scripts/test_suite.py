#! /usr/local/bin/python2.7

import sys, re, subprocess, glob


def main():
  nbtests = 0
  nbsuccess = 0
  argv = sys.argv
  argc = len(argv)
  if argc < 2:
    print("Use ./test_suite.py --help or ./test_suite.py -h")
  elif argv[1] == "-h" or argv[1] == "--help":
    print("./test_suite.py [categories]")
  else:
    topdir = argv[1]
    i = 2
    while i < argc:
      nbtests, nbsuccess = treat_categorie(argv[i], topdir, nbtests, nbsuccess)
      i += 1
  print("\033[1;34mSummary:\033[0m")
  print("Succeeded \033[1;32m"
    + "{0:.0f}".format(float(nbsuccess) / nbtests * 100)
    + "%\033[0m of \033[1;34m" + str(nbtests) + "\033[0m tests in \033[1;34m"
    + str(argc - 2) + "\033[0m categories")
  print("Global success: \033[1;34m" + str(nbsuccess) + "/"
  + str(nbtests) + "\033[0m")

def list_folder(folder, topdir):
  tmp = topdir + "/tests/" + folder + "/"
  return glob.glob(tmp + '*')

def parse_file(p, topdir):
  title = ""
  cmd = ""
  out = ""
  err = ""
  ret = ""
  idx = 0 # 1:title, 2:command, 3:ret, 4:out, 5:err
  f = open(p)
  for l in f:
    if l != "\n":
      if l.lower() == "title\n":
        idx = 1
      elif l.lower() == "command\n":
        idx = 2
      elif l.lower() == "return\n":
        idx = 3
      elif l.lower() == "stdout\n":
        idx = 4
      elif l.lower() == "stderr\n":
        idx = 5
      else:
        if idx == 1:
          title = title + l
        elif idx == 2:
          cmd = cmd + l
          cmd = cmd.replace('$', topdir)
        elif idx == 3:
          ret = ret + l
        elif idx == 4:
          out = out + l
        elif idx == 5:
          err = err + l
  f.close()
  return title.replace('\n', ''), cmd.replace('\n', ''), ret.replace('\n', ''), out, err

def treat_file(f, topdir, nbtests, nbsuccess, catsts, catsucc):
  nbtests += 1
  catsts += 1
  title, cmd, ret, out, err = parse_file(f, topdir)
  print("\n\033[34m\033[4m\033[1mTITLE:\033[0m\033[0m\033[0m " + title)
  print("\033[34m\033[4m\033[1mCOMMAND:\033[0m\033[0m\033[0m " + cmd)
  sub = subprocess.Popen(["sh", "-c", cmd, "2>", "/dev/null"], bufsize = 0,
                         stdout = subprocess.PIPE, stdin = subprocess.PIPE)
  rout, rerr = sub.communicate()
  rret = sub.poll()
  bout = (out == "")
  bret = (ret == "")
  berr = (err == "")
  if (out == rout or bout) and (err == rerr or berr) and (str(rret) == ret or bret):
    print("\n\033[32m\033[1m[SUCCESS]\033[0m\033[0m")
    nbsuccess += 1
    catsucc += 1
  else:
    print("")
    if (out != rout and not(bout)):
      print("\033[33m\033[1mIS :\033[0m\033[0m\n" + rout)
      print("\033[33m\033[1mSTDOUT SHOULD BE :\033[0m\033[0m\n" + out)
    if (err != rerr and not(berr)):
      print("\033[33m\033[1mIS :\033[0m\033[0m\n" + rerr)
      print("\033[33m\033[1mSTDERR SHOULD BE :\033[0m\033[0m\n" + err)
    if (ret != rret and not(bret)):
      print("\033[33m\033[1mGOT "
        + str(rret) + " RETURN VALUE SHOULD BE:\033[0m\033[0m " + ret)
    print("\n\033[31m\033[1m[FAILURE]\033[0m\033[0m")
  return nbtests, nbsuccess, catsts, catsucc

def treat_categorie(categorie, topdir, nbtests, nbsuccess):
    catsts = 0
    catsucc = 0
    print("\t\n\033[33m\033[1m"
      + "----------------------------------------------------------------------------\n"
      + "Category: " + categorie + "\n"
      + "----------------------------------------------------------------------------"
      + "\033[0m\033[0m")
    l = list_folder(categorie, topdir)
    for f in l:
      nbtests, nbsuccess, catsts, catsucc = \
        treat_file(f, topdir, nbtests, nbsuccess, catsts, catsucc)
    print("\nSucceeded \033[1;32m"
      + "{0:.0f}".format((float(catsucc) / catsts * 100))
      + "%\033[0m of \033[1;34m" + str(catsts)
      + "\033[0m tests in category \033[1;34m"
      + categorie +  "\033[0m")
    print("\033[33m\033[1m" +
    "----------------------------------------------------------------------------"
    + "\033[0m\033[0m\n")
    return nbtests, nbsuccess

main()
