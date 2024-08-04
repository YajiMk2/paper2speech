import streamlit as st
from text_file_creator import create_text_file
from text_to_speech import create_audio_file
from translate import translate_abstract
from search_papers import search_papers

def app():
    # Streamlit UI
    st.title("Paper to Speech System")

    # 検索クエリの入力
    query = st.text_input("Enter search query:", value="Retrieval Augmented Generation")

    # ソートオプションの選択
    sort_options = {
        "Relevance": "relevance",
        "Submitted Date": "submittedDate",
        "Last Updated Date": "lastUpdatedDate"
    }
    sort_by = st.selectbox("Sort by", options=list(sort_options.keys()), index=0)

    # 翻訳モデルの選択
    translation_model = st.selectbox("Choose translation model", ["openai", "sentence_transformers"], index=0)

    # 音声変換モデルの選択
    speech_model = st.selectbox("Choose speech conversion model", ["openai", "sentence_transformers"], index=0)

    # 結果数の指定
    max_results = st.number_input("Number of results", min_value=1, max_value=50, value=10)

    # 検索ボタン
    if st.button("Search"):
        with st.spinner("Searching..."):
            papers = search_papers(query, max_results=max_results, sort_by=sort_options[sort_by])

        if papers:
            st.success(f"Found {len(papers)} papers.")
            selected_paper = st.selectbox("Select a paper to process", [p['title'] for p in papers])

            # 論文の詳細を表示
            for paper in papers:
                if paper['title'] == selected_paper:
                    st.write(f"**Title**: {paper['title']}")
                    st.write(f"**Authors**: {', '.join(paper['authors'])}")
                    st.write(f"**Published**: {paper['published']}")
                    st.write(f"**Summary**: {paper['summary']}")

                    # 翻訳と音声化ボタン
                    if st.button("Translate and Generate Audio"):
                        with st.spinner("Translating and generating audio..."):
                            # Abstractの翻訳
                            abstract_jp = translate_abstract(paper['summary'], model=translation_model)

                            # テキストファイルの生成
                            text_file_path = create_text_file(paper['title'], abstract_jp, paper['summary'])

                            # 音声ファイルの生成
                            audio_file_path = create_audio_file(abstract_jp, paper['title'], model=speech_model)

                        st.success("Processing complete.")
                        st.write(f"Generated text file at: {text_file_path}")
                        st.write(f"Generated audio file at: {audio_file_path}")
                        st.audio(audio_file_path)
        else:
            st.error("No papers found.")

if __name__ == "__main__":
    app()
