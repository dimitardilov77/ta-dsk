TEST

# Test 1  
| Field                                 | Instruction                                                                         
| ------------------------------------- | ----------------------------------------------------------------------------------- 
| Name                                  | Check the names are correct 
| Status                                | Draft                 
| Precondition                          | Open practice form at https://demoqa.com/automation-practice-form
| Objective                             | To check if the user input both First and Last name and they are correct        
| Priority                              | High                     
| Owner                                 | Creator                                     
| Estimated                             | 2 min       
| Test Script (Steps) - Step            | Enter the site, input First and Last name and push submit button                                                    
| Test Script (Steps) - Test Data       | Scenario 1: empty, Scenario 2: Ivan Ivanov, Scenario 3 Ivan8 Ivanov                                   
| Test Script (Steps) - Expected Result | Scenario 1: error, Scenario 2: pass, Scenario 3: error    

# Test 2
| Field                                 | Instruction                                                                         
| ------------------------------------- | ----------------------------------------------------------------------------------- 
| Name                                  | Check the email is correct
| Status                                | Draft                 
| Precondition                          | Open practice form at https://demoqa.com/automation-practice-form
| Objective                             | To check if the email format input from the user is correct        
| Priority                              | Medium                     
| Owner                                 | Creator                                     
| Estimated                             | 2 min       
| Test Script (Steps) - Step            | Enter the site, input the emial adress and push submit button                                                    
| Test Script (Steps) - Test Data       | Scenario 1: ivanivanov@gmail.com, Scenario 2: ivan ivanov@gmail.com, Scenario 3: ivanivanovgmail.com                                
| Test Script (Steps) - Expected Result | Scenario 1: pass, Scenario 2: error, Scenario 3: error    

# Test 3
| Field                                 | Instruction                                                                         
| ------------------------------------- | ----------------------------------------------------------------------------------- 
| Name                                  | Check the mobile number is filled in and correct
| Status                                | Draft                 
| Precondition                          | Open practice form at https://demoqa.com/automation-practice-form
| Objective                             | To check if the mobile number is filled in and have at exactly 10 digits       
| Priority                              | High                     
| Owner                                 | Creator                                     
| Estimated                             | 2 min       
| Test Script (Steps) - Step            | Enter the site, input the phone number and push submit button                                                
| Test Script (Steps) - Test Data       | Scenario 1: empty, Scenario 2: 123d455667, Scenario 3: 3456 Scenario 4: 64839281276                               
| Test Script (Steps) - Expected Result | Scenario 1: error, Scenario 2: error, Scenario 3: error, Scenario 4: pass   

# Test 4
| Field                                 | Instruction                                                                         
| ------------------------------------- | ----------------------------------------------------------------------------------- 
| Name                                  | Check if selected picture is in the proper format
| Status                                | Draft                 
| Precondition                          | Open practice form at https://demoqa.com/automation-practice-form
| Objective                             | Check if selected picture is in the proper format. Supported formats: jpg, png, bmp     
| Priority                              | Low                     
| Owner                                 | Creator                                     
| Estimated                             | 2 min       
| Test Script (Steps) - Step            | Enter the site, select choose file, choose a file and click upload.                                               
| Test Script (Steps) - Test Data       | Scenario 1: jpg, Scenario 2: png, Scenario 3: bmp Scenario 4: any other format                               
| Test Script (Steps) - Expected Result | Scenario 1: pass, Scenario 2: pass, Scenario 3: pass, Scenario 4: error  


# Test 5
| Field                                 | Instruction                                                                         
| ------------------------------------- | ----------------------------------------------------------------------------------- 
| Name                                  | Check states and cities
| Status                                | Draft                 
| Precondition                          | Open practice form at https://demoqa.com/automation-practice-form
| Objective                             | Check if for each states there are at least one city to be selected  
| Priority                              | Low                     
| Owner                                 | Creator                                     
| Estimated                             | 2 min       
| Test Script (Steps) - Step            | Enter the site, select a state, select a city                                               
| Test Script (Steps) - Test Data       | Redo it for each single state                              
| Test Script (Steps) - Expected Result | For each state there should be at least 1 city from which to choose in the city dropdown