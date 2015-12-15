# handle a few things that paste-template can't do
# we could get clever here and do git init, git add, etc.
# after it runs, this .mk file is now useless, so we
# delete ourselves.

init:
	chmod +x $(MANAGE)
	mv jscsrc .jscsrc
	rm -f init.mk
