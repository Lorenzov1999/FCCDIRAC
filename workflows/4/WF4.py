#!/bin/env python
"""script to do X"""
from DIRAC.Core.Base.Script import parseCommandLine
parseCommandLine()

from ILCDIRAC.Interfaces.API.NewInterface.Applications import GaudiApp, DelphesApp
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import UserJob
from ILCDIRAC.Interfaces.API.DiracILC import DiracILC

def run():
  """Run The Job."""
  job = UserJob()
  job.setConfigPackage("fccConfig", 'key4hep-devel-2')

  ga = GaudiApp()
  ga.setVersion('key4hep-latest')
  ga.setExecutableName("k4run")
  ga.setSteeringFile('k4simdelphesalg_pythia.py')
  ga.setPythia8Card('p8_ee_ggqq_ecm91.cmd') #p8_ee_ZH_ecm240.cmd p8_ee_WW_ecm240 p8_ee_ZZ_ecm240.cmd
  ga.setExtraCLIArguments("--Pythia8.PythiaInterface.pythiacard pythia8card.cmd --k4SimDelphesAlg.DelphesCard card_IDEA.tcl --k4SimDelphesAlg.DelphesOutputSettings edm4hep_IDEA.tcl")
  ga.setEnergy(91.19)
  ga.setNumberOfEvents(50)
  ga.setOutputFile('output.root')

  job.append(ga)
  job.submit(DiracILC(), mode='local')


if __name__ =="__main__":
  run()