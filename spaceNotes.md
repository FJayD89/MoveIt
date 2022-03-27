how am i going to do this
for every car, if it's paralell to the winDir, check if intersects winPath
for cars other than wincar, there can be paralell cars in front, so check for that as well

when returning multiple values from a function, do we want an object?


passing len=n list is about the same as passing n args
less arguments passed is def better

is it better to make a new block when moving, 
or just increment the existing one and have to decrement it later?
who knows
I should probably actually solve that though

stuff to time:
 - passing everything when recursing vs global
   - nonglobal board = don't have to revert moves
 - making a new block when moving vs changing existing thing
 - comparing an array vs comparing the elements individually

everything global needs to be reverted

dynamic board only needs to be saved as dict{name:pos} -> could try saving seen boards (after)

wincheck:
 - check if winBlock pos == calculated winPos
   - or rather, only the dynamic coordinate is necessary
   - actually, have only the useful winPos coordinate be saved
 - add a pathclear check to see if there are no blocking cars
   - use modified pathclear that returns false immediately when it finds a blocker
   - doesn't need to chceck if a block yields new info, since any info validates a termination
   - doesn't need to actually calculate te distance
   - requires adding a few arguments to winCheck but oh well
