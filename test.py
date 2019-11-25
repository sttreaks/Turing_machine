# def _optimise(self):
#     """That function optimising way on tape. If we need to pass the n same symbols in the same machine state we
#     return the index of the last symbol. If we multiply to ints its great optimisation. Also we check if Machine
#     cycled at 1 state and stay at cell.
#
#     :return: Return actual position for turing machine
#     """
#     current_state = self.r.q[self.cs][self.t._t[self.point]]
#     if self.t._t[self.point] == current_state[0] and self.cs == current_state[1]:
#         if current_state[2] == -1:
#             s = str(self.t._t[::-1]).replace(" ", "")[1:-1]
#             s = s[len(self.t._t) - 1 - self.point:]
#             return self.point - s.find(str(1 - self.t._t[self.point]))
#         elif current_state[2] == 1:
#             s = str(self.t._t).replace(" ", "")[1:-1]
#             s = s[self.point:]
#             return self.point + s.find(str(1 - self.t._t[self.point]))
#         else:
#             return "cycled"
#     return None


# startpos = self.point
# analysed_position = self._optimise()
# if analysed_position is not None:
#     if analysed_position == "cycled":
#         self.cycled = True
#         break
#     self.point = analysed_position
