print(max([(i//900+100)*(i%900+100) for i in range(810000) if str((i//900+100)*(i%900+100))==str((i//900+100)*(i%900+100))[::-1]]))