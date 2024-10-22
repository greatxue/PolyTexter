# README

### Description-featured

1. Remove somewhere:
   ```
   ["arr0"]
   ```
2. Add at chemprop/chemprop/models/model.py: line 90
   ```
    self.X_d_mlp = nn.Sequential(
        nn.Dropout(0.5),
        nn.Linear(4096, 128),
        nn.BatchNorm1d(128),
        nn.ReLU(), 
        nn.Dropout(0.5),
        nn.Linear(128, 128),
        nn.BatchNorm1d(128),
    )
   ```
3. Modify at chemprop/chemprop/models/model.py: function `fingerprint`
   ```
   return H if X_d is None else torch.cat((H, self.X_d_mlp(X_d)), 1)
   ```
4. Modify at chemprop/chemprop/cli/train.py: line 980
   ```
   input_dim = 428, #concat to: 300+128
   ```
