def checkBoxChecker(self):
                self.listWidget.clear()

                ######################################

                if self.radioPadlock.isChecked():
                    if self.chkKey.isChecked():
                            test1 = str("ES146: Key Storage Drop Test")
                            test2 = str("ANSI A156.5-6.3.3: Torque-Cyilinder Plug")
                            self.listWidget.addItem(test1)
                            self.listWidget.addItem(test2)
                    else:
                            ()

                    if self.chkCable.isChecked():
                            test = str("ES128: Cable Testing")
                            self.listWidget.addItem(test)
                    else:
                            ()

                    if self.chkDial.isChecked():
                            test1 = str("MLTS 0017: 1588 Combo Lock Test")
                            test2 = str("ASTM F883.10.2 Combination Padlock Cycle Test")
                            self.listWidget.addItem(test1)
                            self.listWidget.addItem(test2)
                    else:
                            ()

                    if self.chkShackle.isChecked():
                            test1 = str("ES120: Wedge Test")
                            test2 = str("ES000450: Tensile Opening")
                            self.listWidget.addItem(test1)
                            self.listWidget.addItem(test2)
                    else:
                            ()

                    if self.chkOutdoor.isChecked():
                            test1 = str("IEC 60068: Environmental Testing")
                            test2 = str("ASTM F883.11.1: Salt Spray")
                            test3 = str("ASTM F883.11.2: Dry Contaminate Environmental Testing")
                            test4 = str("ASTM F883.11.3: Salt/UV")
                            test5 = str("ASTM F883.11.1: Wet Freezing")
                            self.listWidget.addItem(test1)
                            self.listWidget.addItem(test2)
                            self.listWidget.addItem(test3)
                            self.listWidget.addItem(test4)
                            self.listWidget.addItem(test5)
                    else:
                            ()

                    if self.chkElectronics.isChecked():
                            test = str("MLTS 0014: Bagged Thermal Cycle Test")
                            self.listWidget.addItem(test)
                    else:
                            ()

                    if self.chkLogo.isChecked():
                            test = str("ES 121: Logo Adhesion")
                            self.listWidget.addItem(test)
                    else:
                            ()
                else:
                    ()

    #######################################################

                if self.radioSafe.isChecked():
                    
                    if self.chkSafeDoor.isChecked():
                        test1 = str("WI007031: Pry Test")
                        test2 = str("WI007025: Initial Force Close")
                        self.listWidget.addItem(test1)
                        self.listWidget.addItem(test2)
                        
                        if self.chkSafeVerticalHinge.isChecked():
                            test1 = str("WI007037: Door Top Loading Test Procedure")
                            test2 = str("WI007071: Door Hyper Extension Test")
                            test3 = str("WI007076: Security Safe Door Top Loading Test")
                            self.listWidget.addItem(test1)
                            self.listWidget.addItem(test2)
                            self.listWidget.addItem(test3)
                        else:
                            ()
                        
                        if self.chkSafeHandle.isChecked():
                            test1 = str("WI007032: Shock Test, Rev A")
                            test2 = str("WI007029: SLS Door Handle Actuation Test")
                            self.listWidget.addItem(test1)
                            self.listWidget.addItem(test2)
                            
                            if self.chkSafePlastic.isChecked():
                                test1 = str("WI007018: Plastic Handle Impact Test")
                                test2 = str("WI007019: Plastic Handle Pull (Tension) Test")
                                test3 = str("WI007020: Plastic Handle Torque Test")
                                self.listWidget.addItem(test1)
                                self.listWidget.addItem(test2)
                                self.listWidget.addItem(test3)
                            else:
                                ()
                            
                        else:
                            ()
                        
                    else:
                        ()

                    if self.chkSafeCashBox.isChecked():
                        test = str("WI007046: Cashbox Drop Test")
                        self.listWidget.addItem(test)
                    else:
                        ()

                    if self.chkSafeFireProof.isChecked():
                        test = str("WI007067: Fire Endurance Test")
                        self.listWidget.addItem(test)
                    else:
                        ()
                        
                    if self.chkSafeWaterProof.isChecked():
                        test = str("WI007054: Water Resistant Test For Safes")
                        self.listWidget.addItem(test)
                    else:
                        ()
                        
                    if self.chkSafeKey.isChecked():
                        test1 = str("WI007042: Key Insert Force")
                        test2 = str("WI007040: Key Torque Lock/Unlock")
                        test3 = str("WI007043: Key Lock Actuation")
                        test4 = str("WI007044: Key Torque to Fail")
                        self.listWidget.addItem(test1)
                        self.listWidget.addItem(test2)
                        self.listWidget.addItem(test3)
                        self.listWidget.addItem(test4)
                    else:
                        ()
                    
                    if self.chkSafeElectronics.isChecked():
                        test1 = str("WI007035: Over Voltage")
                        test2 = str("WI007033: Forward & Reverse Voltage")
                        self.listWidget.addItem(test1)
                        self.listWidget.addItem(test2)
                        
                        if self.chkSafeBatteries.isChecked():
                            test1 = str("WI007045: Sleep Current")
                            test2 = str("WI007034: Low Battery Test")
                            test3 = str("WI007022: Battery Life Test")
                            self.listWidget.addItem(test1)
                            self.listWidget.addItem(test2)
                            self.listWidget.addItem(test3)
                        else:
                            ()
                        
                        if self.chkSafeSolenoid.isChecked():
                            test1 = str("WI007021: Solenoid Side Load Test")
                            test2 = str("WI007048: Solenoid Coil Resistance")
                            test3 = str("WI007069: Solenoid Mechanical Stress Test")
                            test4 = str("WI007070: Override Solenoid Test")
                            self.listWidget.addItem(test1)
                            self.listWidget.addItem(test2)
                            self.listWidget.addItem(test3)
                            self.listWidget.addItem(test4)
                        else:
                            ()
                        
                        if self.chkSafeSensors.isChecked():
                            if self.chkSafeHumidity.isChecked():
                                test = str("WI007036: Humidity Sensor Test")
                                self.listWidget.addItem(test)
                            else:
                                ()
                            
                            if self.chkSafeTemperature.isChecked():
                                test = str("WI007036: Temperature Sensor Test")
                                self.listWidget.addItem(test)
                            else:
                                ()
                        else:
                            ()
                    
                    if self.chkSafeDial.isChecked():
                        test = str("WI007041: Dial Clicker Actuation Test")
                        self.listWidget.addItem(test)
                    else:
                        ()
                        
                    if self.chkSafeShelf.isChecked():
                        test1 = str("WI007079: Accessory Load Test")
                        test2 = str("WI007024: Shelf Load Test")
                        self.listWidget.addItem(test1)
                        self.listWidget.addItem(test2)
                    else:
                        ()
                        
                    if self.chkSafePowdercoated.isChecked():
                        test = str("WI007068: Powder Coat Adhesion Test")
                        self.listWidget.addItem(test)
                    else:
                        ()
                else:
                    ()
