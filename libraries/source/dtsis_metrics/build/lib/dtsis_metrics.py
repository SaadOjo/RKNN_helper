from timeit import default_timer as timer

class fps:
	def __init__(self):
		self.accum_time = 0
		self.curr_fps   = 0
		self.prev_time  = timer()
		self.fps = 0

	def update(self):
		self.curr_time = timer()
		self.exec_time = self.curr_time - self.prev_time
		self.prev_time = self.curr_time
		self.accum_time += self.exec_time
		self.curr_fps += 1
		if self.accum_time > 1:
			self.accum_time -= 1 
			self.fps = self.curr_fps
			self.curr_fps = 0

	def get_fps(self):
		return self.fps

class average:
	def __init__(self, N):
		self.pointer = 0
		self.array = np.zeros(N)
		self.N = N
		self.array_filled = False
		self.value = 0
	def update(self, value):
		self.value = value
		self.array[self.pointer] = value
		if self.pointer == self.N - 1:
			self.array_filled = True
		self.pointer = (self.pointer + 1)%self.N	
	def average(self):
		if self.array_filled:
			return self.array.sum() / self.N
		else:
			return self.value
