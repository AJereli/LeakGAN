FROM ufoym/deepo:tensorflow-py27-cu90
#VOLUME vol1

# Install system packages
#RUN \
#     apt-get update && apt-get install \
#         gawk && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


#RUN pip install --upgrade pip
#
#RUN pip install scipy
#
#
#RUN   pip install \
#
#      tensorflow-gpu \
#      cntk-gpu  \
#      matplotlib


ADD convert.py /
ADD dataloader.py /
ADD Discriminator.py /
ADD eval_bleu.py /
ADD LeakGANModel.py /
ADD Main.py /
ADD CommentsMay2017_text.txt /
ADD save save /
ADD speech speech /
ADD ckpts ckpts /
ADD NYT_key_val.txt /
ADD save/experiment-log.txt /
CMD [ "python", "./Main.py" ]