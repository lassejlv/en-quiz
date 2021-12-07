print("Hejsa og velkommen til min første Python-spil!")

ans = input("Er du klar til at spille? (ja/nej)")

score = 0
total_q: 4

if ans.lower() == "nej":
    print("😭 Øv, så længe du ikke er klar, så er det bare sådan!")
    exit()
if ans.lower() == "ja":
    ans = input("🚩 1. Hvad er det bedste programmeringssprog?")
    if ans.lower() == "javascript":
        score += 1
        print("✅ Du svarede rigtigt!")
    else:
        print("❌ Du svarede forkert!")
        score -= 1
        

    ans = input("➗ 2. Hvad giver 1 + 1 + 1 * 0?")
    if ans.lower() == "2":
        score += 2
        print("✅ Du svarede rigtigt!")
    else:
        print("❌ Du svarede forkert! Ærligt jeg troede du var bedere end dette!")
        score -= 1
    
    ans = input("💻 3. Hvad er den bedste code editor?")
    if ans.lower() == "vscode" or ans.lower() == "visual studio code": 
        score += 3
        print("✅ Du svarede rigtigt!")
    else:
        print("❌ Du svarede forkert!")
        score -= 2

if score == 6:
    print("Du har sku vundet! Din score var helt oppe på ", score)

if score != 6:
  print('Du kom igennem med en score på ', score, ' du godt gøre det bedere!')
