import torch
c=torch.arange(1000*0,1000*(0+1)).view(-1)
c = torch.nn.functional.one_hot(c.to(torch.int64),1000).to('cuda').to(torch.float)
print(c.size())