# Alexander - K02 - 13519090
result = []

def totalTime(t,n):
# Asumsi bahwa larik t sudah terurut menaik
  if (n < 3): # Elemen dibawah 3
    if (n == 2):
      result.append([t[n-1],t[n-2]])
    else :
      result.append(t[n-1])
    return t[n - 1]
  elif (n == 3): # Jika larik hanya berisikan 3 elemen
    result.append([t[0],t[1]])
    result.append(t[0])
    result.append([t[0],t[2]])
    return t[0] + t[1] + t[2]
  # larik berisikan lebih atau sama dengan 4 elemen
  else :
    time = t[1] + t[0] + t[n-1] + t[1]
    time2 =  t[n-1] + t[0] + t[n-2] + t[0]

    if time2 < time :
      result.append([t[0],t[n-1]])
      result.append(t[0])
      result.append([t[0],t[n-2]])
      result.append(t[0])
      time = time2 
    else :
      result.append([t[0],t[1]])
      result.append(t[0])
      result.append([t[n-1],t[n-2]])
      result.append(t[1])

  return time + totalTime(t[:-2], len(t[:-2]))

def bridgeAndTorch(problem,bound):
    timeResult = totalTime(problem,len(problem))
    if ( int(timeResult) > int(bound)):
        print ("Solusi tidak mungkin ditemukan, tingkatkan batas waktu")
        print ("Solusi yang ditemukan : ")
    else :
        print("Solusi Ditemukan") 
    print(result)
    print("Total Waktu yang diperlukan : ",timeResult)

def main():
    persoalan = input("Masukkan kecepatan orang, dipisahkan dengan koma : ")
    persoalan = [int(x) for x in persoalan.split(",")]
    persoalan.sort()
    batas = input("Masukkan batas waktu : ")
    bridgeAndTorch(persoalan,batas)

main()


