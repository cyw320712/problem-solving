def solution(records):
    answer = []
    
    user = {}
    history = []
    for record in records:
      srecord = record.split()
      
      cmd = srecord[0]
      uid = srecord[1]
      
      if cmd == "Change":
        name = srecord[2]
        user[uid] = name
      elif cmd == "Enter":
        name = srecord[2]
        user[uid] = name
        history.append((cmd, uid))
      else:
        history.append((cmd, uid))
    
    for h in history:
      cmd = h[0]
      uid = h[1]
      if cmd == "Enter":
        answer.append(f"{user[uid]}님이 들어왔습니다.")
      elif cmd == "Leave":
        answer.append(f"{user[uid]}님이 나갔습니다.")
        
    return answer