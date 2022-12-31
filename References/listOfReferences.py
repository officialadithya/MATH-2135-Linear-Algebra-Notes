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
    title["def"] = "\\textit{Definition}"
    title["thm"] = "\\textit{Theorem}"
    title["exa"] = "\\textit{Example}"
    title["exe"] = "\\textit{Exercise}"
    
    reference = lines[i][lines[i].find("{")+1:lines[i].find("}")]
    lines[i] = title[reference[0:reference.find(":")]]+" \\ref{"+reference+"}, Page \\pageref{"+reference+"} \\\\"
    
nonempty = [i for i in lines if i != ""]
print("\n".join(nonempty))