# I have imported all required libraries here
import os
import time
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad,unpad


# SINCE PLAINTEXT IS NORMAL TEXT IT IS CONVERTED TO BYTES BEFORE ENCRYPTION
# FUNCTION TO CONVERT PLAINTEXT INTO BYTES
def make_bytes(string_ip):
    encoded_text = bytes(string_ip, 'utf-8')
    return encoded_text


#
#   --------------------------------------------ENC-DEC IN CBC------------------------------------------------  #
#
class CBC:
    # DES MODE
    def InDES(plaintext):
        # Converting String data into ByteArray by calling function and passing text
        plaintext = make_bytes(plaintext)
        # 8-byte string key in bytes
        key = b'secret-k'

        # Declaring IV
        iv = b'12345678'
        # ENCRYPT
        start = time.time()
        encipher = DES.new(key, DES.MODE_CBC, iv)
        encrypted_text = encipher.encrypt(pad(plaintext, DES.block_size))  # Pad the input data and then encrypt
        # DECRYPT
        decipher = DES.new(key, DES.MODE_CBC, iv)
        decrypted_text = decipher.decrypt(encrypted_text)
        decrypted_text = unpad(decrypted_text,DES.block_size)
        print('Executed DES in CBC mode time taken->', time.time() - start, 'seconds')


    # 3DES MODE
    def InDES3(plaintext):
        # Converting String data into ByteArray by calling function and passing text
        plaintext = make_bytes(plaintext)
        # Generating 24 byte key ie;
        # key = DES3.adjust_key_parity(get_random_bytes(24))        # This will generate key automatically
        key = b'secretkey123456789012345'  # User defined key manually

        # ENCRYPT
        start = time.time()
        encipher = DES3.new(key, DES3.MODE_CBC, IV=None)
        encrypted_text = encipher.iv + encipher.encrypt(pad(plaintext,DES3.block_size))
        # DECRYPT
        decipher = DES3.new(key, DES3.MODE_CBC, IV=None)
        decrypted_text = decipher.decrypt(encrypted_text)
        decrypted_text = unpad(decrypted_text, DES3.block_size)

        print('Executed 3DES in CBC mode time taken->', time.time() - start, 'seconds')


    # AES MODE
    def InAES(plaintext):
        # Converting String data into ByteArray by calling function and passing text
        plaintext = make_bytes(plaintext)
        key = b'secretkey1234567'  # User defined 16 byte key

        # Declaring IV
        iv = b'1234567890123456'
        # ENCRYPT
        start = time.time()
        encipher = AES.new(key, AES.MODE_CBC,iv)
        encrypted_text = encipher.encrypt(pad(plaintext,AES.block_size))
        # DECRYPT
        decipher = AES.new(key, AES.MODE_CBC,iv)
        decrypted_text = decipher.decrypt(encrypted_text)
        decrypted_text = unpad(decrypted_text, AES.block_size)

        print('Executed AES in CBC mode time taken->', time.time() - start, 'seconds')


#
#   -----------------------------------------ENC-DEC IN ECB------------------------------------------------  #
#
class ECB:
    # DES MODE
    def InDES(plaintext):
        # Converting String data into ByteArray by calling function and passing text
        plaintext = make_bytes(plaintext)
        # 8-byte string key to bytes
        key = b'secret-k'

        # ENCRYPT
        start = time.time()
        encipher = DES.new(key, DES.MODE_ECB)
        encrypted_text = encipher.encrypt(pad(plaintext,DES.block_size))  # Pad the input data and then encrypt
        # DECRYPT
        decipher = DES.new(key, DES.MODE_ECB)
        decrypted_text = decipher.decrypt(encrypted_text)
        decrypted_text = unpad(decrypted_text, DES.block_size)

        print('Executed DES in ECB mode time taken->', time.time() - start, 'seconds')


    # 3DES MODE
    def InDES3(plaintext):
        # Converting String data into ByteArray by calling function and passing text
        plaintext = make_bytes(plaintext)
        # Generating 24 byte key ie
        # key = DES3.adjust_key_parity(get_random_bytes(24))
        key = b'secretkey123456789012345'  # User defined key

        # ENCRYPT
        start = time.time()
        encipher = DES3.new(key, DES3.MODE_ECB)
        encrypted_text = encipher.encrypt(pad(plaintext,DES3.block_size))
        # DECRYPT
        decipher = DES3.new(key, DES3.MODE_ECB)
        decrypted_text = decipher.decrypt(encrypted_text)
        decrypted_text = unpad(decrypted_text, DES3.block_size)

        print('Executed 3DES in ECB mode time taken->', time.time() - start, 'seconds')

    # AES MODE
    def InAES(plaintext):
        # Converting String data into ByteArray by calling function and passing text
        plaintext = make_bytes(plaintext)
        key = b'secretkey1234567'  # User defined 16 byte key

        # ENCRYPT
        start = time.time()
        encipher = AES.new(key, AES.MODE_ECB)
        encrypted_text = encipher.encrypt(pad(plaintext,AES.block_size))
        # DECRYPT
        decipher = AES.new(key, AES.MODE_ECB)
        decrypted_text = decipher.decrypt(encrypted_text)
        decrypted_text = unpad(decrypted_text, AES.block_size)

        print('Executed AES in ECB mode time taken->', time.time() - start, 'seconds')



def callMethods(plaintext):

    # ---------------------CALLING METHODS------------------- #
    # THERE ARE 2 CLASSES, CBC AND ECB, Both have 3 funcs, InDES, InDES3, InAES
    # plaintext is given as input
    # Enc-Dec in DES
    print("\n-- DES --")
    CBC.InDES(plaintext)
    ECB.InDES(plaintext)
    # Enc-Dec in 3DES
    print("\n-- 3DES --")
    CBC.InDES3(plaintext)
    ECB.InDES3(plaintext)
    # Enc-Dec in AES
    print("\n-- AES --")
    CBC.InAES(plaintext)
    ECB.InAES(plaintext)


if __name__ == '__main__':  # MAIN()
# -- CODE BELOW IS FOR IMPORTING TEXT FILE --

    # BELOW 2 LINES PRINT SIZE OF MESSAGE
    # size = os.path.getsize('./Message.txt')
    # print('Text size : ', size / (1024 * 1024), "MB")

# -- Opening Message.txt to read text data stored in it --
    # Below 3 lines import data in Message.txt and read it and saves data in plaintext

    # with open('Message.txt', 'r', encoding='utf-8', errors='ignore') as file:
    #     lines = file.readlines()
    # plainText = ''.join(lines)

    plainText = "hello, I am piyush kumar kondhol1hello, I am piyush kumar kondhol2hello, I am piyush kumar kondhol3hello, I am piyush kumar kondhol4hello, I am piyush kumar kondhol5hello, I am piyush kumar kondhol6hello, I am piyush kumar kondhol7hello, I am piyush kumar kondhol8hello, I am piyush kumar kondhol9hello, I am piyush kumar kondhol10hello, I am piyush kumar kondhol11hello, I am piyush kumar kondhol12hello, I am piyush kumar kondhol13hello, I am piyush kumar kondhol14hello, I am piyush kumar kondhol15hello, I am piyush kumar kondhol16hello, I am piyush kumar kondhol17hello, I am piyush kumar kondhol18hello, I am piyush kumar kondhol19hello, I am piyush kumar kondhol20hello, I am piyush kumar kondhol21hello, I am piyush kumar kondhol22hello, I am piyush kumar kondhol23hello, I am piyush kumar kondhol24hello, I am piyush kumar kondhol25hello, I am piyush kumar kondhol26hello, I am piyush kumar kondhol27hello, I am piyush kumar kondhol28hello, I am piyush kumar kondhol29hello, I am piyush kumar kondhol30hello, I am piyush kumar kondhol31hello, I am piyush kumar kondhol32hello, I am piyush kumar kondhol33hello, I am piyush kumar kondhol34hello, I am piyush kumar kondhol35hello, I am piyush kumar kondhol36hello, I am piyush kumar kondhol37hello, I am piyush kumar kondhol38hello, I am piyush kumar kondhol39hello, I am piyush kumar kondhol40hello, I am piyush kumar kondhol41hello, I am piyush kumar kondhol42hello, I am piyush kumar kondhol43hello, I am piyush kumar kondhol44hello, I am piyush kumar kondhol45hello, I am piyush kumar kondhol46hello, I am piyush kumar kondhol47hello, I am piyush kumar kondhol48hello, I am piyush kumar kondhol49hello, I am piyush kumar kondhol50hello, I am piyush kumar kondhol51hello, I am piyush kumar kondhol52hello, I am piyush kumar kondhol53hello, I am piyush kumar kondhol54hello, I am piyush kumar kondhol55hello, I am piyush kumar kondhol56hello, I am piyush kumar kondhol57hello, I am piyush kumar kondhol58hello, I am piyush kumar kondhol59hello, I am piyush kumar kondhol60hello, I am piyush kumar kondhol61hello, I am piyush kumar kondhol62hello, I am piyush kumar kondhol63hello, I am piyush kumar kondhol64hello, I am piyush kumar kondhol65hello, I am piyush kumar kondhol66hello, I am piyush kumar kondhol67hello, I am piyush kumar kondhol68hello, I am piyush kumar kondhol69hello, I am piyush kumar kondhol70hello, I am piyush kumar kondhol71hello, I am piyush kumar kondhol72hello, I am piyush kumar kondhol73hello, I am piyush kumar kondhol74hello, I am piyush kumar kondhol75hello, I am piyush kumar kondhol76hello, I am piyush kumar kondhol77hello, I am piyush kumar kondhol78hello, I am piyush kumar kondhol79hello, I am piyush kumar kondhol80hello, I am piyush kumar kondhol81hello, I am piyush kumar kondhol82hello, I am piyush kumar kondhol83hello, I am piyush kumar kondhol84hello, I am piyush kumar kondhol85hello, I am piyush kumar kondhol86hello, I am piyush kumar kondhol87hello, I am piyush kumar kondhol88hello, I am piyush kumar kondhol89hello, I am piyush kumar kondhol90hello, I am piyush kumar kondhol91hello, I am piyush kumar kondhol92hello, I am piyush kumar kondhol93hello, I am piyush kumar kondhol94hello, I am piyush kumar kondhol95hello, I am piyush kumar kondhol96hello, I am piyush kumar kondhol97hello, I am piyush kumar kondhol98hello, I am piyush kumar kondhol99hello, I am piyush kumar kondhol100hello, I am piyush kumar kondhol101hello, I am piyush kumar kondhol102hello, I am piyush kumar kondhol103hello, I am piyush kumar kondhol104hello, I am piyush kumar kondhol105hello, I am piyush kumar kondhol106hello, I am piyush kumar kondhol107hello, I am piyush kumar kondhol108hello, I am piyush kumar kondhol109hello, I am piyush kumar kondhol110hello, I am piyush kumar kondhol111hello, I am piyush kumar kondhol112hello, I am piyush kumar kondhol113hello, I am piyush kumar kondhol114hello, I am piyush kumar kondhol115hello, I am piyush kumar kondhol116hello, I am piyush kumar kondhol117hello, I am piyush kumar kondhol118hello, I am piyush kumar kondhol119hello, I am piyush kumar kondhol120hello, I am piyush kumar kondhol121hello, I am piyush kumar kondhol122hello, I am piyush kumar kondhol123hello, I am piyush kumar kondhol124hello, I am piyush kumar kondhol125hello, I am piyush kumar kondhol126hello, I am piyush kumar kondhol127hello, I am piyush kumar kondhol128hello, I am piyush kumar kondhol129hello, I am piyush kumar kondhol130hello, I am piyush kumar kondhol131hello, I am piyush kumar kondhol132hello, I am piyush kumar kondhol133hello, I am piyush kumar kondhol134hello, I am piyush kumar kondhol135hello, I am piyush kumar kondhol136hello, I am piyush kumar kondhol137hello, I am piyush kumar kondhol138hello, I am piyush kumar kondhol139hello, I am piyush kumar kondhol140hello, I am piyush kumar kondhol141hello, I am piyush kumar kondhol142hello, I am piyush kumar kondhol143hello, I am piyush kumar kondhol144hello, I am piyush kumar kondhol145hello, I am piyush kumar kondhol146hello, I am piyush kumar kondhol147hello, I am piyush kumar kondhol148hello, I am piyush kumar kondhol149hello, I am piyush kumar kondhol150hello, I am piyush kumar kondhol151hello, I am piyush kumar kondhol152hello, I am piyush kumar kondhol153hello, I am piyush kumar kondhol154hello, I am piyush kumar kondhol155hello, I am piyush kumar kondhol156hello, I am piyush kumar kondhol157hello, I am piyush kumar kondhol158hello, I am piyush kumar kondhol159hello, I am piyush kumar kondhol160hello, I am piyush kumar kondhol161hello, I am piyush kumar kondhol162hello, I am piyush kumar kondhol163hello, I am piyush kumar kondhol164hello, I am piyush kumar kondhol165hello, I am piyush kumar kondhol166hello, I am piyush kumar kondhol167hello, I am piyush kumar kondhol168hello, I am piyush kumar kondhol169hello, I am piyush kumar kondhol170hello, I am piyush kumar kondhol171hello, I am piyush kumar kondhol172hello, I am piyush kumar kondhol173hello, I am piyush kumar kondhol174hello, I am piyush kumar kondhol175hello, I am piyush kumar kondhol176hello, I am piyush kumar kondhol177hello, I am piyush kumar kondhol178hello, I am piyush kumar kondhol179hello, I am piyush kumar kondhol180hello, I am piyush kumar kondhol181hello, I am piyush kumar kondhol182hello, I am piyush kumar kondhol183hello, I am piyush kumar kondhol184hello, I am piyush kumar kondhol185hello, I am piyush kumar kondhol186hello, I am piyush kumar kondhol187hello, I am piyush kumar kondhol188hello, I am piyush kumar kondhol189hello, I am piyush kumar kondhol190hello, I am piyush kumar kondhol191hello, I am piyush kumar kondhol192hello, I am piyush kumar kondhol193hello, I am piyush kumar kondhol194hello, I am piyush kumar kondhol195hello, I am piyush kumar kondhol196hello, I am piyush kumar kondhol197hello, I am piyush kumar kondhol198hello, I am piyush kumar kondhol199hello, I am piyush kumar kondhol200hello, I am piyush kumar kondhol201hello, I am piyush kumar kondhol202hello, I am piyush kumar kondhol203hello, I am piyush kumar kondhol204hello, I am piyush kumar kondhol205hello, I am piyush kumar kondhol206hello, I am piyush kumar kondhol207hello, I am piyush kumar kondhol208hello, I am piyush kumar kondhol209hello, I am piyush kumar kondhol210hello, I am piyush kumar kondhol211hello, I am piyush kumar kondhol212hello, I am piyush kumar kondhol213hello, I am piyush kumar kondhol214hello, I am piyush kumar kondhol215hello, I am piyush kumar kondhol216hello, I am piyush kumar kondhol217hello, I am piyush kumar kondhol218hello, I am piyush kumar kondhol219hello, I am piyush kumar kondhol220hello, I am piyush kumar kondhol221hello, I am piyush kumar kondhol222hello, I am piyush kumar kondhol223hello, I am piyush kumar kondhol224hello, I am piyush kumar kondhol225hello, I am piyush kumar kondhol226hello, I am piyush kumar kondhol227hello, I am piyush kumar kondhol228hello, I am piyush kumar kondhol229hello, I am piyush kumar kondhol230hello, I am piyush kumar kondhol231hello, I am piyush kumar kondhol232hello, I am piyush kumar kondhol233hello, I am piyush kumar kondhol234hello, I am piyush kumar kondhol235hello, I am piyush kumar kondhol236hello, I am piyush kumar kondhol237hello, I am piyush kumar kondhol238hello, I am piyush kumar kondhol239hello, I am piyush kumar kondhol240hello, I am piyush kumar kondhol241hello, I am piyush kumar kondhol242hello, I am piyush kumar kondhol243hello, I am piyush kumar kondhol244hello, I am piyush kumar kondhol245hello, I am piyush kumar kondhol246hello, I am piyush kumar kondhol247hello, I am piyush kumar kondhol248hello, I am piyush kumar kondhol249hello, I am piyush kumar kondhol250hello, I am piyush kumar kondhol251hello, I am piyush kumar kondhol252hello, I am piyush kumar kondhol253hello, I am piyush kumar kondhol254hello, I am piyush kumar kondhol255hello, I am piyush kumar kondhol256hello, I am piyush kumar kondhol257hello, I am piyush kumar kondhol258hello, I am piyush kumar kondhol259hello, I am piyush kumar kondhol260hello, I am piyush kumar kondhol261hello, I am piyush kumar kondhol262hello, I am piyush kumar kondhol263hello, I am piyush kumar kondhol264hello, I am piyush kumar kondhol265hello, I am piyush kumar kondhol266hello, I am piyush kumar kondhol267hello, I am piyush kumar kondhol268hello, I am piyush kumar kondhol269hello, I am piyush kumar kondhol270hello, I am piyush kumar kondhol271hello, I am piyush kumar kondhol272hello, I am piyush kumar kondhol273hello, I am piyush kumar kondhol274hello, I am piyush kumar kondhol275hello, I am piyush kumar kondhol276hello, I am piyush kumar kondhol277hello, I am piyush kumar kondhol278hello, I am piyush kumar kondhol279hello, I am piyush kumar kondhol280hello, I am piyush kumar kondhol281hello, I am piyush kumar kondhol282hello, I am piyush kumar kondhol283hello, I am piyush kumar kondhol284hello, I am piyush kumar kondhol285hello, I am piyush kumar kondhol286hello, I am piyush kumar kondhol287hello, I am piyush kumar kondhol288hello, I am piyush kumar kondhol289hello, I am piyush kumar kondhol290hello, I am piyush kumar kondhol291hello, I am piyush kumar kondhol292hello, I am piyush kumar kondhol293hello, I am piyush kumar kondhol294hello, I am piyush kumar kondhol295hello, I am piyush kumar kondhol296hello, I am piyush kumar kondhol297hello, I am piyush kumar kondhol298hello, I am piyush kumar kondhol299hello, I am piyush kumar kondhol300hello, I am piyush kumar kondhol301hello, I am piyush kumar kondhol302hello, I am piyush kumar kondhol303hello, I am piyush kumar kondhol304hello, I am piyush kumar kondhol305hello, I am piyush kumar kondhol306hello, I am piyush kumar kondhol307hello, I am piyush kumar kondhol308hello, I am piyush kumar kondhol309hello, I am piyush kumar kondhol310hello, I am piyush kumar kondhol311hello, I am piyush kumar kondhol312hello, I am piyush kumar kondhol313hello, I am piyush kumar kondhol314hello, I am piyush kumar kondhol315hello, I am piyush kumar kondhol316hello, I am piyush kumar kondhol317hello, I am piyush kumar kondhol318hello, I am piyush kumar kondhol319hello, I am piyush kumar kondhol320hello, I am piyush kumar kondhol321hello, I am piyush kumar kondhol322hello, I am piyush kumar kondhol323hello, I am piyush kumar kondhol324hello, I am piyush kumar kondhol325hello, I am piyush kumar kondhol326hello, I am piyush kumar kondhol327hello, I am piyush kumar kondhol328hello, I am piyush kumar kondhol329hello, I am piyush kumar kondhol330hello, I am piyush kumar kondhol331hello, I am piyush kumar kondhol332hello, I am piyush kumar kondhol333hello, I am piyush kumar kondhol334hello, I am piyush kumar kondhol335hello, I am piyush kumar kondhol336hello, I am piyush kumar kondhol337hello, I am piyush kumar kondhol338hello, I am piyush kumar kondhol339hello, I am piyush kumar kondhol340hello, I am piyush kumar kondhol341hello, I am piyush kumar kondhol342hello, I am piyush kumar kondhol343hello, I am piyush kumar kondhol344hello, I am piyush kumar kondhol345hello, I am piyush kumar kondhol346hello, I am piyush kumar kondhol347hello, I am piyush kumar kondhol348hello, I am piyush kumar kondhol349hello, I am piyush kumar kondhol350hello, I am piyush kumar kondhol351hello, I am piyush kumar kondhol352hello, I am piyush kumar kondhol353hello, I am piyush kumar kondhol354hello, I am piyush kumar kondhol355hello, I am piyush kumar kondhol356hello, I am piyush kumar kondhol357hello, I am piyush kumar kondhol358hello, I am piyush kumar kondhol359hello, I am piyush kumar kondhol360hello, I am piyush kumar kondhol361hello, I am piyush kumar kondhol362hello, I am piyush kumar kondhol363hello, I am piyush kumar kondhol364hello, I am piyush kumar kondhol365hello, I am piyush kumar kondhol366hello, I am piyush kumar kondhol367hello, I am piyush kumar kondhol368hello, I am piyush kumar kondhol369hello, I am piyush kumar kondhol370hello, I am piyush kumar kondhol371hello, I am piyush kumar kondhol372hello, I am piyush kumar kondhol373hello, I am piyush kumar kondhol374hello, I am piyush kumar kondhol375hello, I am piyush kumar kondhol376hello, I am piyush kumar kondhol377hello, I am piyush kumar kondhol378hello, I am piyush kumar kondhol379hello, I am piyush kumar kondhol380hello, I am piyush kumar kondhol381hello, I am piyush kumar kondhol382hello, I am piyush kumar kondhol383hello, I am piyush kumar kondhol384hello, I am piyush kumar kondhol385hello, I am piyush kumar kondhol386hello, I am piyush kumar kondhol387hello, I am piyush kumar kondhol388hello, I am piyush kumar kondhol389hello, I am piyush kumar kondhol390hello, I am piyush kumar kondhol391hello, I am piyush kumar kondhol392hello, I am piyush kumar kondhol393hello, I am piyush kumar kondhol394hello, I am piyush kumar kondhol395hello, I am piyush kumar kondhol396hello, I am piyush kumar kondhol397hello, I am piyush kumar kondhol398hello, I am piyush kumar kondhol399hello, I am piyush kumar kondhol400hello, I am piyush kumar kondhol401hello, I am piyush kumar kondhol402hello, I am piyush kumar kondhol403hello, I am piyush kumar kondhol404hello, I am piyush kumar kondhol405hello, I am piyush kumar kondhol406hello, I am piyush kumar kondhol407hello, I am piyush kumar kondhol408hello, I am piyush kumar kondhol409hello, I am piyush kumar kondhol410hello, I am piyush kumar kondhol411hello, I am piyush kumar kondhol412hello, I am piyush kumar kondhol413hello, I am piyush kumar kondhol414hello, I am piyush kumar kondhol415hello, I am piyush kumar kondhol416hello, I am piyush kumar kondhol417hello, I am piyush kumar kondhol418hello, I am piyush kumar kondhol419hello, I am piyush kumar kondhol420hello, I am piyush kumar kondhol421hello, I am piyush kumar kondhol422hello, I am piyush kumar kondhol423hello, I am piyush kumar kondhol424hello, I am piyush kumar kondhol425hello, I am piyush kumar kondhol426hello, I am piyush kumar kondhol427hello, I am piyush kumar kondhol428hello, I am piyush kumar kondhol429hello, I am piyush kumar kondhol430hello, I am piyush kumar kondhol431hello, I am piyush kumar kondhol432hello, I am piyush kumar kondhol433hello, I am piyush kumar kondhol434hello, I am piyush kumar kondhol435hello, I am piyush kumar kondhol436hello, I am piyush kumar kondhol437hello, I am piyush kumar kondhol438hello, I am piyush kumar kondhol439hello, I am piyush kumar kondhol440hello, I am piyush kumar kondhol441hello, I am piyush kumar kondhol442hello, I am piyush kumar kondhol443hello, I am piyush kumar kondhol444hello, I am piyush kumar kondhol445hello, I am piyush kumar kondhol446hello, I am piyush kumar kondhol447hello, I am piyush kumar kondhol448hello, I am piyush kumar kondhol449hello, I am piyush kumar kondhol450hello, I am piyush kumar kondhol451hello, I am piyush kumar kondhol452hello, I am piyush kumar kondhol453hello, I am piyush kumar kondhol454hello, I am piyush kumar kondhol455hello, I am piyush kumar kondhol456hello, I am piyush kumar kondhol457hello, I am piyush kumar kondhol458hello, I am piyush kumar kondhol459hello, I am piyush kumar kondhol460hello, I am piyush kumar kondhol461hello, I am piyush kumar kondhol462hello, I am piyush kumar kondhol463hello, I am piyush kumar kondhol464hello, I am piyush kumar kondhol465hello, I am piyush kumar kondhol466hello, I am piyush kumar kondhol467hello, I am piyush kumar kondhol468hello, I am piyush kumar kondhol469hello, I am piyush kumar kondhol470hello, I am piyush kumar kondhol471hello, I am piyush kumar kondhol472hello, I am piyush kumar kondhol473hello, I am piyush kumar kondhol474hello, I am piyush kumar kondhol475hello, I am piyush kumar kondhol476hello, I am piyush kumar kondhol477hello, I am piyush kumar kondhol478hello, I am piyush kumar kondhol479hello, I am piyush kumar kondhol480hello, I am piyush kumar kondhol481hello, I am piyush kumar kondhol482hello, I am piyush kumar kondhol483hello, I am piyush kumar kondhol484hello, I am piyush kumar kondhol485hello, I am piyush kumar kondhol486hello, I am piyush kumar kondhol487hello, I am piyush kumar kondhol488hello, I am piyush kumar kondhol489hello, I am piyush kumar kondhol490hello, I am piyush kumar kondhol491hello, I am piyush kumar kondhol492hello, I am piyush kumar kondhol493hello, I am piyush kumar kondhol494hello, I am piyush kumar kondhol495hello, I am piyush kumar kondhol496hello, I am piyush kumar kondhol497hello, I am piyush kumar kondhol498hello, I am piyush kumar kondhol499"

    callMethods(plainText)  # CALLING CallMethods()
