{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kmAyush/Video-Dubbing-with-Lip-Synchronization/blob/main/Text%20Translation/trans_text.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "XrFAu2_6v_XV"
      },
      "outputs": [],
      "source": [
        "import pickle\n",
        "import torch\n",
        "import torch.nn as nn\n",
        "import torch.nn.functional as F\n",
        "import gdown"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "url = \"https://drive.google.com/file/d/1-3yAkoJtKfNyr5bHh2qayuQVOeMYTPVO/view?usp=drive_link\"\n",
        "!mkdir -p tokenizer\n",
        "id = url.split('/')[-2]\n",
        "file_url = f'https://drive.google.com/uc?id={id}'\n",
        "destination_location = \"/content/Video-Dubbing-with-Lip-Synchronization/Text Translation/\"\n",
        "gdown.download(file_url , destination_location, quiet=False )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 105
        },
        "id": "WIcueAag0wTw",
        "outputId": "6196e170-b2b1-4fbf-c315-41bbc8c0de13"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Downloading...\n",
            "From: https://drive.google.com/uc?id=1-3yAkoJtKfNyr5bHh2qayuQVOeMYTPVO\n",
            "To: /content/tokenizer/english.pkl\n",
            "100%|██████████| 741k/741k [00:00<00:00, 98.0MB/s]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'/content/tokenizer/english.pkl'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "url = \"https://drive.google.com/file/d/1-ACb3okGOeYACwCofyOIVla6udM5gVnl/view?usp=drive_link\"\n",
        "id = url.split('/')[-2]\n",
        "file_url = f'https://drive.google.com/uc?id={id}'\n",
        "destination_location = \"/content/Video-Dubbing-with-Lip-Synchronization/Text Translation/\"\n",
        "gdown.download(file_url , destination_location, quiet=False )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 105
        },
        "id": "trI-iImd0wWx",
        "outputId": "4a0906d0-fdb9-40b5-e562-05a2675db8ac"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Downloading...\n",
            "From: https://drive.google.com/uc?id=1-ACb3okGOeYACwCofyOIVla6udM5gVnl\n",
            "To: /content/tokenizer/hindi.pkl\n",
            "100%|██████████| 1.08M/1.08M [00:00<00:00, 122MB/s]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'/content/tokenizer/hindi.pkl'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "url = \"https://drive.google.com/file/d/1-Dd_CTPUDG40FmGXUJQ3G7SfMFhTPgJL/view?usp=sharing\"\n",
        "id = url.split('/')[-2]\n",
        "file_url = f'https://drive.google.com/uc?id={id}'\n",
        "destination_location = \"/content/Video-Dubbing-with-Lip-Synchronization/Text Translation/\"\n",
        "gdown.download(file_url , destination_location, quiet=False )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 122
        },
        "id": "HNGNDb4_18BQ",
        "outputId": "63694a6d-05fd-49ad-9875-bf725c9098ac"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Downloading...\n",
            "From (original): https://drive.google.com/uc?id=1-Dd_CTPUDG40FmGXUJQ3G7SfMFhTPgJL\n",
            "From (redirected): https://drive.google.com/uc?id=1-Dd_CTPUDG40FmGXUJQ3G7SfMFhTPgJL&confirm=t&uuid=fd55db81-97e2-4025-ba12-9d7b8e10f01b\n",
            "To: /content/model/bidir_word_clip_model.pt\n",
            "100%|██████████| 404M/404M [00:02<00:00, 197MB/s]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'/content/model/bidir_word_clip_model.pt'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "file_path = '/content/Video-Dubbing-with-Lip-Synchronization/Text Translation/english.pkl'\n",
        "\n",
        "with open(file_path, 'rb') as file:\n",
        "   tokenizer_eng = pickle.load(file)\n",
        "\n",
        "\n",
        "file_path = '/content/Video-Dubbing-with-Lip-Synchronization/Text Translation/hindi.pkl'\n",
        "\n",
        "with open(file_path, 'rb') as file:\n",
        "   tokenizer_hin = pickle.load(file)\n",
        "\n",
        "eng_vocab = tokenizer_eng.get_vocab()\n",
        "hin_vocab = tokenizer_hin.get_vocab()\n"
      ],
      "metadata": {
        "id": "fJxHA5R6xToP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class AttentionModule(torch.nn.Module):\n",
        "    \"\"\" Implements an attention module \"\"\"\n",
        "    def __init__(self, input_size):\n",
        "        \"\"\" Initializes the attention module.\n",
        "            Feel free to declare any parameters as required. \"\"\"\n",
        "\n",
        "        super(AttentionModule, self).__init__()\n",
        "\n",
        "        self.W_key = nn.Linear((2*input_size), input_size)\n",
        "        self.W_query = nn.Linear(input_size, input_size)\n",
        "        self.W_value =nn.Linear((2*input_size), input_size)\n",
        "\n",
        "\n",
        "    def forward(self, encoder_outputs, decoder_hidden_state):\n",
        "        \"\"\" Performs a forward pass over the module, computing attention scores for inputs.\n",
        "\n",
        "        Args:\n",
        "            encoder_outputs (torch.Tensor): Output representations from the encoder, of shape [batch_size?, src_seq_len, output_dim].\n",
        "            decoder_hidden_state (torch.Tensor): Hidden state from the decoder at current time step, of appropriate shape as per RNN unit (with optional batch dim).\n",
        "\n",
        "        Returns:\n",
        "            torch.Tensor: Attentions scores for given inputs, of shape [batch_size?, 1, src_seq_len]\n",
        "        \"\"\"\n",
        "        keys = self.W_key(encoder_outputs)  # batch,seq_length, hidden_size\n",
        "        values = self.W_value(encoder_outputs)   # batch,seq_length, hidden_size\n",
        "\n",
        "        # decoder_hidden_state ==  num_layer,N, hid_size\n",
        "\n",
        "        num_layers = decoder_hidden_state.size(0)\n",
        "        decoder_hidden_state = decoder_hidden_state[num_layers-1].unsqueeze(1)  # N , 1, hidden\n",
        "        query = self.W_query(decoder_hidden_state)  #  batch,1 ,hidden_size\n",
        "        query = query.transpose(1, 2)  # (batch size, hidden size, 1)\n",
        "\n",
        "        weights = torch.matmul(keys, query)  # batch , sequence, 1\n",
        "        weights = F.softmax(weights, dim = 1)   # (batch, sequence,  1)\n",
        "\n",
        "        context_vector = weights * values  # N, seq_length , hidden\n",
        "\n",
        "        context_vector = torch.sum(context_vector, dim = 1, keepdim = True) # N, 1, hidden\n",
        "\n",
        "        return context_vector, weights"
      ],
      "metadata": {
        "id": "e8gMHwv5xTrl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "## ==== BEGIN EVALUATION PORTION\n",
        "\n",
        "class RNNEncoderDecoderLMWithAttention(torch.nn.Module):\n",
        "    \"\"\" Implements an Encoder-Decoder network, using RNN units, augmented with attention. \"\"\"\n",
        "\n",
        "    # Feel free to add additional parameters to __init__\n",
        "    def __init__(self,src_vocab_size, tgt_vocab_size, embd_dims, hidden_size, num_layers=1, dropout=0.1, teacher_force_ratio = 1 ):\n",
        "        \"\"\" Initializes the encoder-decoder network, implemented via RNNs.\n",
        "\n",
        "        Args:\n",
        "            src_vocab_size (int): Source vocabulary size.\n",
        "            tgt_vocab_size (int): Target vocabulary size.\n",
        "            embd_dims (int): Embedding dimensions.\n",
        "            hidden_size (int): Size/Dimensions for the hidden states.\n",
        "        \"\"\"\n",
        "\n",
        "        super(RNNEncoderDecoderLMWithAttention, self).__init__()\n",
        "\n",
        "        self._dummy_param = torch.nn.Parameter(torch.Tensor(0), requires_grad=False)\n",
        "\n",
        "        self.src_vocab_size = src_vocab_size\n",
        "        self.tgt_vocab_size = tgt_vocab_size\n",
        "\n",
        "        self.num_layers = num_layers\n",
        "        self.hidden_size = hidden_size\n",
        "\n",
        "        self.dropout_enc = nn.Dropout(dropout)\n",
        "        self.dropout_dec = nn.Dropout(dropout)\n",
        "        self.teacher_force_ratio = teacher_force_ratio\n",
        "        self.enc_pad_index = 0\n",
        "\n",
        "        self.tgt_pad_index = 0\n",
        "        self.tgt_start_index = 1\n",
        "        self.tgt_end_index = 2\n",
        "\n",
        "        self.attension_module = AttentionModule(hidden_size)\n",
        "\n",
        "        self.encoder_embedding = torch.nn.Embedding(src_vocab_size, embd_dims)\n",
        "        self.encoder_lstm = nn.LSTM(embd_dims, hidden_size,num_layers = num_layers , batch_first = True, dropout = dropout, bidirectional=True)\n",
        "\n",
        "        self.decoder_embedding = torch.nn.Embedding(tgt_vocab_size, embd_dims)\n",
        "        self.decoder_lstm = nn.LSTM(embd_dims+hidden_size, hidden_size,num_layers = num_layers, batch_first = True, dropout = dropout)\n",
        "        self.decoder_output_fc = nn.Linear(hidden_size, embd_dims)\n",
        "        self.dec_out_embed = nn.Linear(embd_dims,tgt_vocab_size, bias = False)\n",
        "\n",
        "        self.dec_out_embed.weight = self.decoder_embedding.weight\n",
        "\n",
        "    @property\n",
        "    def device(self):\n",
        "        return self._dummy_param.device\n",
        "\n",
        "    def forward(self, inputs, decoder_inputs=None, decoder_hidden_state=None, output_attention=False ):\n",
        "        \"\"\" Performs a forward pass over the encoder-decoder network.\n",
        "\n",
        "            Accepts inputs for the encoder, inputs for the decoder, and hidden state for\n",
        "                the decoder to continue generation after the given input.\n",
        "\n",
        "        Args:\n",
        "            inputs (torch.Tensor): tensor of shape [batch_size?, src_seq_len]\n",
        "            decoder_inputs (torch.Tensor): Decoder inputs, as tensor of shape [batch_size?, 1]\n",
        "            decoder_hidden_state (any): tensor to represent decoder hidden state from time step T-1.\n",
        "            output_attention (bool): If true, this function should also return the\n",
        "                associated attention weights for the time step, of shape [batch_size?, 1, src_seq_len].\n",
        "\n",
        "        Returns:\n",
        "            tuple[torch.Tensor, any]: output from the decoder, and associated hidden state for the next step.\n",
        "\n",
        "            Decoder outputs should be log probabilities over the target vocabulary.\n",
        "\n",
        "        Example:\n",
        "        >>> model = RNNEncoderDecoderWithAttention(*args, **kwargs)\n",
        "        >>> output, hidden = model(..., output_attention=False)\n",
        "        >>> output, hidden, attn_weights = model(..., output_attention=True)\n",
        "        \"\"\"\n",
        "\n",
        "        batch_size = inputs.size(0)\n",
        "        seq_length = decoder_inputs.size(1) if decoder_inputs != None else inputs.size(1)\n",
        "        encoder_input_embed = self.encoder_embedding(inputs)\n",
        "        encoder_output, (encoder_hidden ,cell_encoder )= self.encoder_lstm(encoder_input_embed)\n",
        "\n",
        "        decoder_hidden = encoder_hidden[:self.num_layers,:,:]\n",
        "        decoder_cell = cell_encoder[:self.num_layers,:,:]\n",
        "        decoder_input_test = torch.empty(batch_size, 1, dtype=torch.long, device=device).fill_(self.tgt_start_index)\n",
        "\n",
        "\n",
        "        pred_output_prob = []\n",
        "        weights  = []\n",
        "        for i in range(1,seq_length):\n",
        "\n",
        "            decoder_input_embed = self.decoder_embedding(decoder_input_test)\n",
        "            context_vector, wts = self.attension_module(encoder_output, decoder_hidden)\n",
        "            decoder_input_lstm = torch.cat((decoder_input_embed, context_vector), dim = 2)\n",
        "\n",
        "            dec_output, (decoder_hidden,decoder_cell) = self.decoder_lstm(decoder_input_lstm, (decoder_hidden,decoder_cell))\n",
        "            out_tgt = self.decoder_output_fc(dec_output)\n",
        "            out_tgt_embd = self.dec_out_embed(out_tgt)\n",
        "            pred_output = F.log_softmax(out_tgt_embd, dim = -1)\n",
        "\n",
        "            if decoder_inputs != None:\n",
        "              teacher_frc = torch.rand(1, 1)\n",
        "              if teacher_frc < self.teacher_force_ratio:\n",
        "                 decoder_input_test = decoder_inputs[:, i].unsqueeze(1)\n",
        "\n",
        "              else:\n",
        "                 _, topi = pred_output.topk(1)\n",
        "                 decoder_input_test = topi.squeeze(-1).detach()\n",
        "            else:\n",
        "               _, topi = pred_output.topk(1)\n",
        "               decoder_input_test = topi.squeeze(-1).detach()\n",
        "\n",
        "            pred_output_prob.append(pred_output)\n",
        "            wts = wts.squeeze(0).squeeze(1)\n",
        "            weights.append(wts)\n",
        "\n",
        "\n",
        "        pred_output_prob = torch.cat(pred_output_prob, dim = 1)\n",
        "        weights = torch.stack(weights)\n",
        "\n",
        "\n",
        "        return pred_output_prob,weights"
      ],
      "metadata": {
        "id": "7kFosek3xTwQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "rnn_enc_dec_attn_params = {\n",
        "    'src_vocab_size': len(eng_vocab),\n",
        "    'tgt_vocab_size': len(hin_vocab),\n",
        "    'embd_dims'     : 400,\n",
        "    'hidden_size'   : 800,\n",
        "    'dropout'       : 0.3,\n",
        "    'num_layers'    : 4,\n",
        "    'teacher_force_ratio' : 0.6\n",
        "}\n",
        "\n",
        "device = 'cuda' if torch.cuda.is_available() else 'cpu'\n",
        "model_path = '/content/Video-Dubbing-with-Lip-Synchronization/Text Translation/bidir_word_clip_model.pt'\n",
        "model_state_dict = torch.load(model_path,map_location = device)\n",
        "\n",
        "model = RNNEncoderDecoderLMWithAttention(**rnn_enc_dec_attn_params)\n",
        "model.load_state_dict(model_state_dict)\n",
        "\n",
        "device = 'cuda' if torch.cuda.is_available() else 'cpu'\n",
        "model = model.to(device)"
      ],
      "metadata": {
        "id": "J5UDhJ5-IVtZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def remove_paddings(sequence,pad_token):\n",
        "  while(sequence[-1] == pad_token):\n",
        "    sequence = sequence[:-1]\n",
        "\n",
        "  return sequence\n",
        "\n",
        "def rnn_greedy_generate(seq_x, max_length=5):\n",
        "    \"\"\" Given a source string, translate it to the target language using the trained model.\n",
        "        This function should perform greedy sampling to generate the results.\n",
        "\n",
        "    Args:\n",
        "        model (nn.Module): RNN Type Encoder-Decoder Model\n",
        "        seq_x (str): Input string to translate.\n",
        "        src_tokenizer (Tokenizer): Source language tokenizer.\n",
        "        tgt_tokenizer (Tokenizer): Target language tokenizer.\n",
        "        max_length (int): Maximum length of the target sequence to decode.\n",
        "\n",
        "    Returns:\n",
        "        str: Generated string for the given input in the target language.\n",
        "    \"\"\"\n",
        "\n",
        "    device = 'cuda' if torch.cuda.is_available() else 'cpu'\n",
        "    input_length = len(seq_x)\n",
        "\n",
        "    model.eval()\n",
        "\n",
        "    input_tokens = torch.tensor(seq_x).unsqueeze(0)\n",
        "    input_tokens = input_tokens.to(device)\n",
        "\n",
        "    output_probs,_ = model(input_tokens)\n",
        "    tgt_tokens = torch.argmax(output_probs, dim = 2).squeeze(0).tolist()\n",
        "\n",
        "    tgt_tokens = remove_paddings(tgt_tokens,0)\n",
        "    trans_seq = tokenizer_hin.decode(tgt_tokens[:-1])\n",
        "\n",
        "    return trans_seq"
      ],
      "metadata": {
        "id": "bYTHw5gXxTzs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def generate_trans_text(eng_text):\n",
        "  seq_x = tokenizer_eng.encode(\"<SOS>\").ids+ tokenizer_eng.encode(eng_text).ids + tokenizer_eng.encode(\"<EOS>\").ids\n",
        "  trans_text = rnn_greedy_generate(model,seq_x)\n",
        "  return trans_text\n"
      ],
      "metadata": {
        "id": "G8mDL0H6x0-n"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}