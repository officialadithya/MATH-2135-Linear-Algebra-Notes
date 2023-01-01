from collections import defaultdict

lines = []
with open("main.aux") as f:

  lines = [i.strip() for i in f.readlines()]

for i, _ in enumerate(lines):

  if "\\newlabel" not in lines[i]: lines[i] = ""
    
  else:
    
    title = defaultdict(str)
    title["chapter"] = "\\textbf{Chapter}"
    title["appendix"] = "\\textbf{Appendix}"
    title["def"] = "\\textsc{Definition}"
    title["thm"] = "\\textsc{Theorem}"
    
    reference = lines[i][lines[i].find("{")+1:lines[i].find("}")]
    header = title[reference[0:reference.find(":")]]
    line = header+" \\ref{"+reference+"}, \\textsc{Page} \\pageref{"+reference+"}"
    
    if not (header == "\\textbf{Chapter}" or header == "\\textbf{Appendix}"):
      lines[i] = line+" \\textit{"+lines[i][lines[i].find("\\,\\,")+4:lines[i].find("tcb")-2]+"}"
      
    else: lines[i] = line
      
    lines[i] += " \\\\"
    
nonempty = [i for i in lines if i != "" and i[0] != " "]
print("\n".join(nonempty))