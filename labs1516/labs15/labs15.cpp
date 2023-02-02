//рекурсивные обходы + нерекурсивный

#include <iostream>
#include <string>
#include <vector>

struct BinaryNode
{
	int value;
	BinaryNode* left = nullptr, * right = nullptr;

	
	BinaryNode(std::string& s) //обработка исходной строки
	{
		value = getValue(s);
		s.erase(0, digits(value));
		if (s[0] == '(') s = unbracket(s); 
		else return;
		if (isDigit(s[0])) 
			left = new BinaryNode(s);
		if (s[0] == ',' && isDigit(s[1])) 
			right = new BinaryNode(s.erase(0, 1));
	}

private:
	bool isDigit(char c) { return c >= '0' && c <= '9'; }
	int digits(int n) { return n ? floor(log10(n) + 1) : 1; }

	int getValue(std::string& s)
	{
		int n = s.size(), i = 1;
		while (i < n) 
			if (!isDigit(s[i++])) break;
		return std::stoi(s.substr(0, i));
	}

	std::string unbracket(std::string s) 
	{
		for (int i = 1, d = 1; i < s.size(); i++, d += (s[i] == '(') - (s[i] == ')'))
			if (!d) return s.erase(0, 1).erase(i - 1, 1);
		return s;
	}
};

class BinaryTree
{
	BinaryNode* root = nullptr;

public:
	BinaryTree(std::string s) : root(new BinaryNode(s)) {}

	void directTraverse(BinaryNode* n) //прямой обход
	{
		if (!n) return;
		std::cout << n->value << " ";
		directTraverse(n->left);
		directTraverse(n->right);
	}
	void directTraverse() { directTraverse(root); std::cout << "\n"; }

	void symTraverse(BinaryNode* n) //центрированный обход
	{
		if (!n) return;
		symTraverse(n->left);
		std::cout << n->value << " ";
		symTraverse(n->right);
	}
	void symTraverse() { symTraverse(root); std::cout << "\n"; }

	void inverseTraverse(BinaryNode* n) //концевой обход
	{
		if (!n) return;
		inverseTraverse(n->left);
		inverseTraverse(n->right);
		std::cout << n->value << " ";
	}
	void inverseTraverse() { inverseTraverse(root); std::cout << "\n"; }

	void nonRecursive()
	{
		std::vector<BinaryNode*> stack = { root };
		while (!stack.empty())
		{
			BinaryNode* n = stack.back();
			stack.pop_back();
			std::cout << n->value << " ";
			if (n->right)
				stack.push_back(n->right);
			if (n->left)
				stack.push_back(n->left);
		}
		std::cout << "\n";
	}
};

int main()
{
	BinaryTree tree("8(3(1,6(4,7)),10(,14(13,)))");
	tree.directTraverse();  //прямой 
	tree.symTraverse();     //симметричный
	tree.inverseTraverse(); //концевой
	tree.nonRecursive();
}