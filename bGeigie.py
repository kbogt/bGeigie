class bGeigie:
    def __init__(self, fname):
        self.fname=fname
        self.rawdata=[]
        self.rawlines=[]

    def readData(self):
        f=open(self.fname)
        self.rawdata=f.readlines()
        f.close()

    def dataPoint(self, point):
        rdata={} #return data
        data=point.strip().split(',')
        if data[0] != '$BNRDD':
            raise IndexError()
        else:
            rdata['DevID']=data[1] #device ID
            rdata['UTC']=data[2] #UTC time Zulu format
            rdata['CPM']=data[3] #Counts per minute 
            rdata['C5S']=data[4] #Counts five seconds
            rdata['TCN']=data[5] #Total count number
            rdata['VD']=data[6] #Validated data
            rdata['LAT']=data[7] #Latitude
            rdata['NS']=data[8] #NS
            rdata['LON']=data[9] #Longitude
            rdata['EW']=data[10] #EW
            rdata['GA']=data[11] #GPS acurancy (not sure)
            rdata['PA']=data[12] #Position Accepted
            rdata['NOS']=data[13] #Number of satelites
            rdata['AFIX']=data[14].split('*')[0] #Altitude fix
            rdata['CSum']=data[14].split('*')[1] #CheckSum
            return rdata

    def utcFix(self, Coord, Direction):
        if Direction in ('N','E'):
            sign=''
        else:
            sign='-'
        rd=float(Coord)
        deg=int(rd/100)
        minutes=float(int(rd%100))/60+(rd%1)/60
        return sign+str(deg+minutes)

    def gisData(self, name):
        wf=open(name,'w')
        wf.write('id,value,captured_at,latitude,longitude\n') #file header
        self.readData()
        for line in self.rawdata:
            try:
                rd=self.dataPoint(line)
                #print self.utcFix(rd['LAT'],rd['NS'])
                #print self.utcFix(rd['LON'],rd['EW'])
                wf.write(rd['TCN']+','+rd['CPM']+','+rd['UTC'].split('T')[0]+','+self.utcFix(rd['LAT'],rd['NS'])+','+self.utcFix(rd['LON'],rd['EW'])+'\n')
            except IndexError:
                pass
        wf.close()
        
