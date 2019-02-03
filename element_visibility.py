import time
from utilities.pretty_debug import pretty_debug as debug
# Class to search for element visibility
class element_visibility():

    def __init__(self,browser, command, type='xpath', action='GetText', times=30, clear_popups_xpath=False,ajax=False, classfunc=False):

        # Initialize class variables
        self.iterator_count = 1
        self.iteration_limit = times
        self.browser = browser
        self.comm = command
        self.op_type = type
        self.op_action = action
        self.ajax = ajax
        self.netTrial = 0
        self.clear_popups = clear_popups_xpath
        self.classFunc = classfunc

    # Execute the command
    def search(self):

        # Loop until either element is found or iteration_limit is reached
        while(self.iterator_count <= self.iteration_limit):

            if(self.clear_popups):
                try:
                    self.browser.find_element_by_xpath("{}".format(self.clear_popups)).click()
                    debug("Popup cleared")
                except Exception as p:
                    debug(self.clear_popups)
                    debug("Popup not cleared {}".format(p))

            if(self.classFunc):
                try:
                    self.classFunc(self.browser)
                except Exception as t:
                    debug("the class function excption {}".format(t))

            # Try executing command
            try:
                debug("Running element_visibility in iteration {0}".format(self.iterator_count))
                self.iterator_count = self.iterator_count + 1


                if (self.op_type == "xpath"):

                    if(self.op_action == "click"):
                        # Exit if element is found
                        self.browser.find_element_by_xpath("{}".format(self.comm)).click()
                        self.iterator_count = self.iteration_limit + 1

                    elif(self.op_action == "GetText"):
                        # data = ""
                        data = str(self.browser.find_element_by_xpath("{}".format(self.comm)).text)

                        '''try:
                            data = str(self.browser.find_element_by_xpath("{}".format(self.comm)).text)

                        except NoSuchElementException as r:
                            debug("the NoSuchElementException is {}".format(r))

                        except Exception as t:
                            debug("General Exception is {}".format(t))'''


                        if(data != ""):
                            # debug("{}".format(data))
                            return data

                    elif (self.op_action == "GetElementCount"):
                        # time.sleep(15)
                        elements = len(self.browser.find_elements_by_xpath("{}".format(self.comm)))

                        if(elements < 1 ):
                            raise Exception("This element is not visible")

                        return elements

                    elif(self.op_action == "GetElements"):
                        # time.sleep(15)
                        elements = self.browser.find_elements_by_xpath("{}".format(self.comm))

                        if (len(elements) < 1):
                            debug(elements)
                            raise Exception("This element is not visible")

                        return elements

                    elif (self.op_action == "ReturnElement"):
                        # time.sleep(15)
                        element = self.browser.find_element_by_xpath("{}".format(self.comm))

                        return element

                    else:
                        debug("What you are trying to do is not defined","This {} action is not defined".format(self.op_action))
                        exit()


                elif (self.op_type == "class_name"):

                    if (self.op_action == "click"):
                        # Exit if element is found
                        self.browser.find_element_by_class_name("{}".format(self.comm)).click()
                        self.iterator_count = self.iteration_limit + 1

                    elif (self.op_action == "GetText"):

                        data = str(self.browser.find_element_by_class_name("{}".format(self.comm)).text)

                        if (data != ""):
                            # debug("{}".format(data))
                            return data

                    elif (self.op_action == "GetElementCount"):
                        # time.sleep(15)
                        elements = len(self.browser.find_element_by_class_name("{}".format(self.comm)))

                        if (elements < 1):
                            return None#raise Exception("This element is not visible")

                        return elements

                    elif (self.op_action == "GetElements"):
                        # time.sleep(15)
                        elements = self.browser.find_element_by_class_name("{}".format(self.comm))

                        if (len(elements) < 1):
                            raise Exception("This element is not visible")

                        return elements

                    else:
                        debug("What you are trying to do is not defined","This {} action is not defined".format(self.op_action))
                        exit()

                else:
                    debug("action not set")

                # debug("Running element_visibility in iteration {0}".format(self.iterator_count)

            #except NoSuchElementException as e:
                #debug("the exception is {}".format(e))

            except Exception as e:
                if (self.iterator_count == self.iteration_limit):
                    debug("Exhausted limit", e)
                    ex = "Element not found {}".format(str(e))

                    # Do this if for some reason the network is down
                    if(self.netTrial == 0 and self.ajax == False and self.iterator_count > 30):
                        debug("Retrying 15 times because we suspect a poor network connection")
                        self.netTrial = self.netTrial + 1
                        self.browser.refresh()
                        self.browser.refresh()
                        time.sleep(7)
                        self.iterator_count = self.iteration_limit - 15

                    else:
                        raise Exception(ex)
                    # return None
                else:

                    debug("Element visibility Exception :{} iteration_limit: {} current iterator_count: {}".format(self.comm, self.iteration_limit,self.iterator_count ), e)

            # Sleep for 1 second and try again
            time.sleep(1)