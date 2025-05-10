"""
It is the process of matching the selenium speed with the browser speed

HOW TO ACHIEVE-->
We can go for 4 ways:
1)time.sleep

2)implicitly wait
check only one state
whether element is present in th dom
by default
no need to write it manually

applicable where the findelement and findelements is present

driver.implicitly_wait()
after maximizing do this step before get

3)Explicit wait
check state of element
by manually
to utilize this explicit wait
we need to proviide two steps
i)create wendriverWait(one time process)
ii)provide  condition based on the state of the webelement (may be multiple time0

checking clickabilit
invisibility of an element
checking visibility
alert is present
located

states means--enabled/disabled
4)fluent Wait

"""
