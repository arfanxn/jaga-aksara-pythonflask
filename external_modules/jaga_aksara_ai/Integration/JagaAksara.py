import os, sys

class JagaAksara:
    def __init__(self, models_folder):
        self.models_folder =  models_folder

        ocr = 'OCR.tflite'
        nlp = 'NLP.tflite'
        
        if not os.path.exists(self.models_folder):
            print(f'Error: folder {self.models_folder} not found')
            sys.exit(1)

        print('successfully set the models folder')

        ocr_path = os.path.join(self.models_folder, ocr)
        nlp_path = os.path.join(self.models_folder, nlp)

        if not os.path.isfile(ocr_path):
            print('Error: OCR AI models not found')
            sys.exit(1)

        if not os.path.isfile(nlp_path):
            print('Error: NLP AI models not found')
            sys.exit(1)
        
        print('successfully load the AI model')

    def ocr(self, image_path):
        if os.path.isfile(image_path):
            return 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vel mi dui. Nunc vitae urna porttitor, fringilla lectus sed, blandit quam. Cras condimentum, purus id tincidunt ultricies, arcu tortor fringilla eros, ac consectetur neque ex vitae tortor. Maecenas sed felis enim. Vivamus venenatis pharetra mauris, et tristique augue fringilla nec. Nullam gravida bibendum laoreet. Nam lacinia nisi et diam ornare congue. Nulla a placerat arcu. Aliquam non ornare diam, ut consequat ligula. Praesent sit amet viverra est. Duis lobortis porttitor orci, sit amet feugiat tortor mollis mollis. Fusce dictum eu felis non sodales. Sed rutrum quam et urna pellentesque, id aliquam augue sollicitudin. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Ut ac imperdiet erat.\nDonec mollis elit eu ipsum porta, sit amet luctus dolor volutpat. In et nulla gravida, dapibus leo at, tempus magna. Integer eu quam neque. Nunc scelerisque egestas felis, eget consequat nulla. Suspendisse faucibus non elit nec iaculis. Curabitur dictum cursus dui, et blandit risus tempor eu. Vivamus suscipit efficitur metus ut tincidunt. Phasellus egestas elit sit amet leo tristique elementum at viverra nibh. Morbi commodo rhoncus condimentum. Phasellus aliquam quam in est accumsan, eu tincidunt libero finibus. Proin tortor ligula, eleifend non vulputate id, molestie et neque. Sed in aliquam nibh. Ut faucibus dignissim libero eu lobortis.\nDonec congue, arcu ut vestibulum interdum, mi quam facilisis arcu, sed pellentesque libero orci quis neque. Suspendisse potenti. Pellentesque eu diam metus. Fusce pulvinar eros eu efficitur auctor. Vestibulum cursus velit a urna elementum fermentum. Aenean vehicula sed dolor a congue. Integer in mi a turpis gravida porttitor id eget ex. Mauris pulvinar magna eu sem laoreet, ac dignissim ex placerat. Nulla pulvinar pulvinar dignissim. Maecenas bibendum libero tortor, quis efficitur velit semper vel. Nam vulputate lacinia venenatis. Nullam dictum arcu eget quam scelerisque, tincidunt consectetur est condimentum. Nam eget faucibus magna, sit amet viverra enim.'
        else:
            print(f'Error: image {image_path} not found')
            sys.exit(1)